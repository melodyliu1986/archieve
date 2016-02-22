__author__ = "ftan"

import csv

from flask import Flask, render_template, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from werkzeug import secure_filename
from peewee import fn

from forms import *
from utils import *


app = Flask(__name__)

# Don't use CSRF
# app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    create_form = CreateAccount(csrf_enabled=False)
    entitle_form = EntitleAccount(csrf_enabled=False)
    csv_form = CreateFormCSV(csrf_enabled=False)
    search_product_form = SearchByProduct(csrf_enabled=False)
    search_name_form = SearchByName(csrf_enabled=False)
    search_attribute_form = SearchBySkuAttribute(csrf_enabled=False)
    search_eng_form = SearchByEngAttribute(csrf_enabled=False)
    refresh_form = RefreshAccount(csrf_enabled=False)
    view_form = ViewAccount(csrf_enabled=False)
    export_form = ExportAccount(csrf_enabled=False)
    delete_form = DeletePool(csrf_enabled=False)

    #######################
    # Create Accounts Tab #
    #######################
    if create_form.validate_on_submit():
        logging.info("====== Create an account ======")
        username = str(create_form.username_create.data).strip()
        password = str(create_form.password_create.data).strip()
        first_name = str(create_form.first_name_create.data).strip()
        last_name = str(create_form.last_name_create.data).strip()
        skus = str(create_form.sku_create.data).strip()
        quantity = create_form.quantity_create.data
        accept = create_form.accept_create.data
        sku_pass = ""
        sku_fail = ""
        sku_con_fail = ""
        sku_inactive = ""
        sku_not_exist = ""
        if first_name == "":
            first_name = "Default"
        if last_name == "":
            last_name = "User"
        logging.info("*Username: %s" % username)
        logging.info("*Password: %s" % password)
        logging.info("First Name: %s" % first_name)
        logging.info("Last Name: %s" % last_name)
        logging.info("Subscription SKUs: %s" % skus)
        logging.info("Quantity: %s" % quantity)
        result = 0
        # check if user exists, if yes, return 1, if no, return 0
        if not check_user(username):
            result = 4
            return render_template(
                        'create.html',
                        username=username,
                        host=host,
                        result=result
                        )
        org_id = find_or_create_user(username, password, first_name, last_name)
        if int(quantity) <= 0:
            sku_fail = str_append(sku_fail, skus.upper())
        elif skus != "" and quantity != "":
            for sku in [i.strip() for i in skus.split(',')]:
                try:
                    # check if sku exists in database
                    if check_sku(sku) == 1:
                        sku_not_exist = str_append(sku_not_exist, sku.upper())
                        continue
                    regnum = hock_sku(username, sku, quantity)
                    if regnum == None:
                        sku_con_fail = str_append(sku_con_fail, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    if activate_regnum(username, org_id, regnum):
                        sku_inactive = str_append(sku_inactive, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    sku_pass = str_append(sku_pass, sku.upper())
                except Exception:
                    sku_fail = str_append(sku_fail, sku.upper())
                    logging.error("Failed to add SKU %s into Account %s" % (sku, username))
        if accept == True:
            i = 0
            while check_accept_terms(username, password):
                logging.info("Accept Terms")
                accept_terms(org_id, username, password)
                logging.info("Refresh")
                i += 1
                if i == 5:
                    break
            result = refresh_account(username)
        logging.info("====== End: Create an account ======")
        return render_template(
                        'create.html',
                        username=username,
                        host=host,
                        result=result,
                        skus=skus,
                        sku_pass=sku_pass,
                        sku_fail=sku_fail,
                        sku_con_fail=sku_con_fail,
                        sku_inactive=sku_inactive,
                        sku_not_exist=sku_not_exist
                        )

    ##############################
    # Add Subscription Pools Tab #
    ##############################
    if entitle_form.validate_on_submit():
        logging.info("====== Add Subscriptions Pool ======")
        username = str(entitle_form.username_entitle.data).strip()
        password = str(entitle_form.password_entitle.data).strip()
        skus = str(entitle_form.sku_entitle.data).strip()
        quantity = entitle_form.quantity_entitle.data
        accept = entitle_form.accept_entitle.data
        result = 0
        sku_pass = ""
        sku_fail = ""
        sku_con_fail = ""
        sku_inactive = ""
        sku_not_exist = ""
        logging.info("*Username: %s" % username)
        logging.info("*Password: %s" % password)
        logging.info("Subscription SKUs: %s" % skus)
        logging.info("Quantity: %s" % quantity)
        # check if password is correct, if yes, return 0, if no, return 2
        if check_password(username, password):
            result = 2
            return render_template(
                            'entitle.html',
                            username=username,
                            sku=skus,
                            result=result
                            )
        org_id = find_or_create_user(username, password)
        logging.info("Org Id for user %s : %s" % (username, org_id))
        if skus != "" and quantity != "":
            for sku in [i.strip() for i in skus.split(',')]:
                try:
                    # check if sku exists in database
                    if check_sku(sku) == 1:
                        sku_not_exist = str_append(sku_not_exist, sku.upper())
                        continue
                    regnum = hock_sku(username, sku, quantity)
                    if regnum == None:
                        sku_con_fail = str_append(sku_con_fail, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    if activate_regnum(username, org_id, regnum):
                        sku_inactive = str_append(sku_inactive, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    sku_pass = str_append(sku_pass, sku.upper())
                except Exception:
                    sku_fail = str_append(sku_fail, sku.upper())
                    logging.error("Failed to add SKU %s into Account %s" % (sku, username))
        if accept == True:
            i = 0
            while check_accept_terms(username, password):
                logging.info("Accept Terms")
                accept_terms(org_id, username, password)
                logging.info("Refresh")
                i += 1
                if i == 5:
                    break
            result = refresh_account(username)
        logging.info("====== End: Add Subscriptions Pool ======")
        return render_template(
                            'entitle.html',
                            username=username,
                            sku=skus,
                            sku_pass=sku_pass,
                            sku_fail=sku_fail,
                            sku_con_fail=sku_con_fail,
                            sku_inactive=sku_inactive,
                            sku_not_exist=sku_not_exist,
                            result=result
                            )

    ################################
    # Create Accounts from CSV Tab #
    ################################
    if csv_form.validate_on_submit():
        logging.info("====== Create Accounts from CSV ======")
        # Save the uploaded vsv file into ./log/csv/ directory
        csv_par_path = './log/'
        csv_path = 'csv/'
        csv_filename = "%s%scsv-%s.csv" % (csv_par_path, csv_path, time.strftime('%Y-%m-%d-%H-%I-%M-%S',time.localtime(time.time())))
        if not os.path.exists(csv_par_path):
            os.mkdir(csv_par_path)
        if not os.path.exists(csv_par_path+csv_path):
            os.mkdir(csv_par_path+csv_path)
        file = request.files['file_csv']
        filename = secure_filename(file.filename)
        file.save("{0}".format(csv_filename))
        csv_file = csv.reader(open("{0}".format(csv_filename), 'rb'))

        accept = csv_form.accept_csv.data

        result = 0
        summary = {}
        summary_list = []
        failed_refresh = []
        logging.info("CSV File: %s" % filename)
        logging.debug("Content of CSV file %s:" % filename)
        logging.debug(csv_file)

        for line in csv_file:
            logging.info("*** Line: %s" % line)
            if line == []:
                continue
            username = line[0].strip()
            password = line[1].strip()
            if password == "":
                password = "redhat"
            summary = {}
            summary["user_info"] = "%s, %s" % (username, password)
            logging.info("Created - user_info: %s" % summary["user_info"])
            failed_sku = ""
            passed_sku = ""
            length = len(line)
            org_id = find_or_create_user(username, password)
            for data in line[2::2]:
                try:
                    sku = data.strip()
                    if sku == "":
                        continue
                    # check if sku exists in database
                    if check_sku(sku) == 1:
                        failed_sku = str_append(failed_sku, sku.upper())
                        continue
                    index = line.index(data) + 1
                    if index < length:
                        quantity = line[index]
                        if int(quantity) <= 0:
                            failed_sku = str_append(failed_sku, sku.upper())
                            continue
                    else:
                        continue
                    regnum = hock_sku(username, sku, quantity)
                    if regnum == None:
                        failed_sku = str_append(failed_sku, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    if activate_regnum(username, org_id, regnum):
                        failed_sku = str_append(failed_sku, sku.upper())
                        logging.error("Failed to add SKU %s into Account %s" % (sku, username))
                        continue
                    passed_sku = str_append(passed_sku, sku.upper())
                except Exception:
                    failed_sku = str_append(failed_sku, sku.upper())
                    logging.error("Failed to add SKU %s into Account %s" % (sku, username))
            if accept == True:
                i = 0
                while check_accept_terms(username, password):
                    accept_terms(org_id, username, password)
                    i += 1
                    if i == 5:
                        break
                result = refresh_account(username)
                if result == 3:
                    failed_refresh.append(username)
            if failed_sku != "":
                summary["fail"] = "Failed to add SKUs: %s" % failed_sku
                logging.info("%s - %s" % (username, summary["fail"]))
            else:
                summary["fail"] = ""
            if passed_sku != "":
                summary["pass"] = "Succeed to add SKUs: %s" % passed_sku
                logging.info("%s - %s" % (username, summary["pass"]))
            else:
                summary["pass"] = ""
            summary_list.append(summary)
        logging.info("====== End: Create Accounts from CSV ======")
        return render_template(
                            'csv.html',
                            file=filename,
                            summary_list=summary_list,
                            failed_refresh=failed_refresh,
                            result=result
                            )

    ###########################################################
    ##  Search Subscription SKUs - Search by Product Family  ##
    ###########################################################
    if search_product_form.validate_on_submit():
        logging.info("====== Search Subscription SKUs - Search by Product Family ======")
        data = search_product_form.data_search_product.data
        logging.info("Product Name to search: %s" % data)
        sku_matrix = []
        sku_failed_matrix = ""
        search_data = "%%%s%%" % data.lower()
        for row in SkuEntry.select().where(fn.Lower(SkuEntry.ph_product_name) % search_data):
            meta = {}
            meta["SKU"] = row.id
            meta['Product Hierarchy: Product Category'] = row.ph_category
            meta['Product Hierarchy: Product Line'] = row.ph_product_line
            meta['Product Hierarchy: Product Name'] = row.ph_product_name
            meta['Product Name'] = row.name
            meta['Virt Limit'] = row.virt_limit
            meta['Socket(s)'] = row.sockets
            meta['VCPU'] = row.vcpu
            meta['Multiplier'] = row.multiplier
            meta['Unlimited Product'] = row.unlimited_product
            meta['Required Consumer Type'] = row.requires_consumer_type
            meta['Product Family'] = row.product_family
            meta['Management Enabled'] = row.management_enabled
            meta['Variant'] = row.variant
            meta['Support Level'] = row.support_level
            meta['Support Type'] = row.support_type
            meta['Enabled Consumer Types'] = row.enabled_consumer_types
            meta['Virt-only'] = row.virt_only
            meta['Cores'] = row.cores
            meta['JON Management'] = row.jon_management
            meta['RAM'] = row.ram
            meta['Instance Based Virt Multiplier'] = row.instance_multiplier
            meta['Cloud Access Enabled'] = row.cloud_access_enabled
            meta['Stacking ID'] = row.stacking_id
            meta['Multi Entitlement'] = row.multi_entitlement
            meta['Host Limited'] = row.host_limited
            meta['Derived SKU'] = row.derived_sku
            meta['Eng Productid(s)'] = row.eng_product_ids
            meta['Arch'] = row.arch
            meta['Username'] = row.username
            sku_matrix.append(meta)
        if data == "":
            data = "ALL Products"
        logging.info("====== End: Search Subscription SKUs - Search by Product Family ======")
        return render_template(
                            'search.html',
                            data=data,
                            sku_matrix=sku_matrix,
                            sku_failed_matrix=sku_failed_matrix,
                            )

    #####################################################
    ##  Search Subscription SKUs - Search by SKU Name  ##
    #####################################################
    if search_name_form.validate_on_submit():
        logging.info("====== Search Subscription SKUs - Search by SKU Name ======")
        skus = search_name_form.data_search_name.data
        logging.info("SKU Name to search: %s" % skus)
        sku_matrix = []
        sku_failed_matrix = ""
        for sku in set(skus.split(',')):
            success = 1
            for row in SkuEntry.select().where(fn.Lower(SkuEntry.id) == sku.strip().lower()):
                success = 0
                meta = {}
                meta["SKU"] = row.id
                meta['Product Hierarchy: Product Category'] = row.ph_category
                meta['Product Hierarchy: Product Line'] = row.ph_product_line
                meta['Product Hierarchy: Product Name'] = row.ph_product_name
                meta['Product Name'] = row.name
                meta['Virt Limit'] = row.virt_limit
                meta['Socket(s)'] = row.sockets
                meta['VCPU'] = row.vcpu
                meta['Multiplier'] = row.multiplier
                meta['Unlimited Product'] = row.unlimited_product
                meta['Required Consumer Type'] = row.requires_consumer_type
                meta['Product Family'] = row.product_family
                meta['Management Enabled'] = row.management_enabled
                meta['Variant'] = row.variant
                meta['Support Level'] = row.support_level
                meta['Support Type'] = row.support_type
                meta['Enabled Consumer Types'] = row.enabled_consumer_types
                meta['Virt-only'] = row.virt_only
                meta['Cores'] = row.cores
                meta['JON Management'] = row.jon_management
                meta['RAM'] = row.ram
                meta['Instance Based Virt Multiplier'] = row.instance_multiplier
                meta['Cloud Access Enabled'] = row.cloud_access_enabled
                meta['Stacking ID'] = row.stacking_id
                meta['Multi Entitlement'] = row.multi_entitlement
                meta['Host Limited'] = row.host_limited
                meta['Derived SKU'] = row.derived_sku
                meta['Eng Productid(s)'] = row.eng_product_ids
                meta['Arch'] = row.arch
                meta['Username'] = row.username
                sku_matrix.append(meta)
            if success == 1:
                sku_failed_matrix = str_append(sku_failed_matrix, sku)
        if len(sku_failed_matrix) != 0:
            logging.error("Failed to get sku %s" % sku_failed_matrix)
        logging.info("====== End: Search Subscription SKUs - Search by SKU Name ======")
        if len(sku_matrix) == 0:
            return render_template(
                                'search_failed.html',
                                data=skus,
                                sku_failed_matrix=sku_failed_matrix
                                )
        else:
            return render_template(
                                'search.html',
                                data=skus,
                                sku_matrix=sku_matrix,
                                sku_failed_matrix=sku_failed_matrix,
                                )

    ###########################################################
    #  Search Subscription SKUs - Search by SKU Attribute     #
    ###########################################################
    if search_attribute_form.validate_on_submit():
        # Total 5 attribute value.
        logging.info("====== Search Subscription SKUs - Search by SKU Attribute ======")

        attribute1 = search_attribute_form.data_search_attribute1.data
        attribute1_text = search_attribute_form.data_search_attribute_text1.data
        attribute2 = search_attribute_form.data_search_attribute2.data
        attribute2_text = search_attribute_form.data_search_attribute_text2.data
        attribute3 = search_attribute_form.data_search_attribute3.data
        attribute3_text = search_attribute_form.data_search_attribute_text3.data
        attribute4 = search_attribute_form.data_search_attribute4.data
        attribute4_text = search_attribute_form.data_search_attribute_text4.data
        attribute5 = search_attribute_form.data_search_attribute5.data
        attribute5_text = search_attribute_form.data_search_attribute_text5.data

        search_attribute = "{0}:{1}, {2}:{3}, {4}:{5}, {6}:{7}, {8}:{9}".format(attribute1, attribute1_text,
                                                                                attribute2, attribute2_text,
                                                                                attribute3, attribute3_text,
                                                                                attribute4, attribute4_text,
                                                                                attribute5, attribute5_text)

        sku_matrix = []
        sku_failed_matrix = ""
        search_attribute_text1 = "%%%s%%" % attribute1_text.lower()
        search_attribute_text2 = "%%%s%%" % attribute2_text.lower()
        search_attribute_text3 = "%%%s%%" % attribute3_text.lower()
        search_attribute_text4 = "%%%s%%" % attribute4_text.lower()
        search_attribute_text5 = "%%%s%%" % attribute5_text.lower()
        search_str1 = "SkuEntry.{0}".format(attribute1)
        search_str2 = "SkuEntry.{0}".format(attribute2)
        search_str3 = "SkuEntry.{0}".format(attribute3)
        search_str4 = "SkuEntry.{0}".format(attribute4)
        search_str5 = "SkuEntry.{0}".format(attribute5)

        search_result = SkuEntry.select().where((fn.Lower(eval(search_str1)) % search_attribute_text1) &
                                                (fn.Lower(eval(search_str2)) % search_attribute_text2) &
                                                (fn.Lower(eval(search_str3)) % search_attribute_text3) &
                                                (fn.Lower(eval(search_str4)) % search_attribute_text4) &
                                                (fn.Lower(eval(search_str5)) % search_attribute_text5))

        success = 1
        for row in search_result:
            success = 0
            meta = {}
            meta["SKU"] = row.id
            meta['Product Hierarchy: Product Category'] = row.ph_category
            meta['Product Hierarchy: Product Line'] = row.ph_product_line
            meta['Product Hierarchy: Product Name'] = row.ph_product_name
            meta['Product Name'] = row.name
            meta['Virt Limit'] = row.virt_limit
            meta['Socket(s)'] = row.sockets
            meta['VCPU'] = row.vcpu
            meta['Multiplier'] = row.multiplier
            meta['Unlimited Product'] = row.unlimited_product
            meta['Required Consumer Type'] = row.requires_consumer_type
            meta['Product Family'] = row.product_family
            meta['Management Enabled'] = row.management_enabled
            meta['Variant'] = row.variant
            meta['Support Level'] = row.support_level
            meta['Support Type'] = row.support_type
            meta['Enabled Consumer Types'] = row.enabled_consumer_types
            meta['Virt-only'] = row.virt_only
            meta['Cores'] = row.cores
            meta['JON Management'] = row.jon_management
            meta['RAM'] = row.ram
            meta['Instance Based Virt Multiplier'] = row.instance_multiplier
            meta['Cloud Access Enabled'] = row.cloud_access_enabled
            meta['Stacking ID'] = row.stacking_id
            meta['Multi Entitlement'] = row.multi_entitlement
            meta['Host Limited'] = row.host_limited
            meta['Derived SKU'] = row.derived_sku
            meta['Eng Productid(s)'] = row.eng_product_ids
            meta['Arch'] = row.arch
            meta['Username'] = row.username
            sku_matrix.append(meta)

        logging.info("====== End: Search Subscription SKUs - Search by SKU Attribute ======")
        if success == 1:
            return render_template('search_failed.html', sku_failed_matrix=sku_failed_matrix)
        else:
            return render_template('search.html', data=search_attribute, sku_matrix=sku_matrix, sku_failed_matrix=sku_failed_matrix)

    ###########################################################
    #  Search Subscription SKUs - Search by Eng Attribute     #
    ###########################################################
    if search_eng_form.validate_on_submit():
        logging.info("====== Search Subscription SKUs - Search by Eng Attribute ======")

        eng_data = search_eng_form.data_search_eng.data
        print "*"*20
        print eng_data, set(eng_data.split(','))

        search_attribute = "Eng Product Id(s):{0}".format(eng_data)
        sku_matrix = []
        sku_failed_matrix = ""

        for eng in set(eng_data.split(',')):
            success = 1
            search_data = "%%%s%%" % eng.strip().lower()
            for row in SkuEntry.select().where(fn.Lower(SkuEntry.eng_product_ids) % search_data):
                success = 0
                meta = {}
                meta["SKU"] = row.id
                meta['Product Hierarchy: Product Category'] = row.ph_category
                meta['Product Hierarchy: Product Line'] = row.ph_product_line
                meta['Product Hierarchy: Product Name'] = row.ph_product_name
                meta['Product Name'] = row.name
                meta['Virt Limit'] = row.virt_limit
                meta['Socket(s)'] = row.sockets
                meta['VCPU'] = row.vcpu
                meta['Multiplier'] = row.multiplier
                meta['Unlimited Product'] = row.unlimited_product
                meta['Required Consumer Type'] = row.requires_consumer_type
                meta['Product Family'] = row.product_family
                meta['Management Enabled'] = row.management_enabled
                meta['Variant'] = row.variant
                meta['Support Level'] = row.support_level
                meta['Support Type'] = row.support_type
                meta['Enabled Consumer Types'] = row.enabled_consumer_types
                meta['Virt-only'] = row.virt_only
                meta['Cores'] = row.cores
                meta['JON Management'] = row.jon_management
                meta['RAM'] = row.ram
                meta['Instance Based Virt Multiplier'] = row.instance_multiplier
                meta['Cloud Access Enabled'] = row.cloud_access_enabled
                meta['Stacking ID'] = row.stacking_id
                meta['Multi Entitlement'] = row.multi_entitlement
                meta['Host Limited'] = row.host_limited
                meta['Derived SKU'] = row.derived_sku
                meta['Eng Productid(s)'] = row.eng_product_ids
                meta['Arch'] = row.arch
                meta['Username'] = row.username
                if meta not in sku_matrix:
                    sku_matrix.append(meta)
            if success == 1:
                sku_failed_matrix = str_append(sku_failed_matrix, eng)
        if len(sku_failed_matrix) != 0:
            logging.error("Failed to get sku %s" % sku_failed_matrix)
        logging.info("====== End: Search Subscription SKUs - Search by SKU Name ======")
        if len(sku_matrix) == 0:
            return render_template(
                                'search_failed.html',
                                data=search_attribute,
                                sku_failed_matrix=sku_failed_matrix
                                )
        else:
            return render_template(
                                'search.html',
                                data=search_attribute,
                                sku_matrix=sku_matrix,
                                sku_failed_matrix=sku_failed_matrix,
                                )

    ######################################
    # Manage - Delete Pools Tab #
    ######################################
    if delete_form.validate_on_submit():
        logging.info("====== Delete Pools ======")
        pool = str(delete_form.pool_delete)
        return "I am working on the code, please wait..."
        result = 0
        result = delete_pools(pool)
        logging.info("====== End: Delete Pools ======")
        return render_template(
                            'delete.html',
                            pool=pool,
                            result=result
                            )

    ######################################
    # Manage - Refresh Subscriptions Tab #
    ######################################
    if refresh_form.validate_on_submit():
        logging.info("====== Refresh Subscription Pools ======")
        username = str(refresh_form.username_refresh.data).strip()
        password = str(refresh_form.password_refresh.data).strip()
        logging.info("Accounts to refresh: %s" % username)

        # check if user exists, if yes, return 0, if no, return 1
        if check_user(username):
            result = 1
            return render_template(
                            'refresh.html',
                            username=username,
                            result=result
                            )
        # check if password is correct, if yes, return 0, if no, return 1
        if check_password(username, password):
            result = 2
            return render_template(
                            'refresh.html',
                            username=username,
                            result=result
                            )
        result = refresh_account(username)
        logging.info("====== End: Refresh Subscription Pools ======")
        return render_template(
                            'refresh.html',
                            username=username,
                            result=result
                            )

    ################################
    # Manage - Export Accounts Tab #
    ################################
    if export_form.validate_on_submit():
        logging.info("====== Export Accounts ======")
        accounts_info = str(export_form.username_export.data).strip()
        logging.info("Accounts to export: %s" % accounts_info)
        account_info_list = accounts_info.split(',')
        info, quantity_mark, quantity_unlimited = account_info(account_info_list)
        logging.info("====== End: Export Account ======")
        return render_template(
                            'export.html',
                            info=info,
                            quantity_mark=quantity_mark,
                            quantity_unlimited=quantity_unlimited,
                            host=host
                            )


    ##############################
    # Manage - View Accounts Tab #
    ##############################
    if view_form.validate_on_submit():
        logging.info("====== View Accounts ======")
        accounts_info = view_form.username_view.data
        logging.info("Accounts to View: %s" % accounts_info)
        account_info_list = accounts_info.split(',')
        info, quantity_mark, quantity_unlimited = account_info(account_info_list)
        logging.info("====== End: View Accounts ======")
        return render_template(
                            'view.html',
                            info=info,
                            quantity_mark=quantity_mark,
                            quantity_unlimited=quantity_unlimited,
                            host=host
                            )

    return render_template(
                        'index.html',
                        create_form=create_form,
                        entitle_form=entitle_form,
                        refresh_form=refresh_form,
                        delete_form=delete_form,
                        view_form=view_form,
                        search_product_form=search_product_form,
                        search_name_form=search_name_form,
                        search_attribute_form=search_attribute_form,
                        search_eng_form=search_eng_form,
                        csv_form=csv_form,
                        export_form=export_form
                        )


if __name__ == '__main__':
    log_file()
    logging.info("====== Start/Reload Account Tool APP ======")
    #manager.run()
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)




