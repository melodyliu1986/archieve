__author__ = 'liusong'
from utils import *

# The attributes. key is the displayed attribute name, value is the attribute name in candlepin.
Attributes_dict_list = [{"--Select Attribute--": "--Select Attribute--"},
                      {"SKU": "id"},
                      {"Product Hierarchy: Product Category": "ph_category"},
                      {"Product Hierarchy: Product Line": "ph_product_line"},
                      {"Product Hierarchy: Product Name": "ph_product_name"},
                      {"Product Name": "name"},
                      {"Virt Limit": "virt_limit"},
                      {"Socket(s)": "sockets"},
                      {"VCPU": "vcpu"},
                      {"Multiplier": "multiplier"},
                      {"Unlimited Product": "unlimited_product"},
                      {"Required Consumer Type": "requires_consumer_type"},
                      {"Product Family": "product_family"},
                      {"Management Enabled": "jon_management"},
                      {"Variant": "variant"},
                      {"Support Level": "support_level"},
                      {"Support Type": "support_type"},
                      {"Enabled Consumer Types": "enabled_consumer_types"},
                      {"Virt-only": "virt_only"},
                      {"Cores": "cores"},
                      {"JON Management": "jon_management"},
                      {"RAM": "ram"},
                      {"Instance Based Virt Multiplier": "instance_multiplier"},
                      {"Cloud Access Enabled": "cloud_access_enabled"},
                      {"Stacking ID": "stacking_id"},
                      {"Multi Entitlement": "multi_entitlement"},
                      {"Host Limited": "host_limited"},
                      {"Derived SKU": "derived_sku"},
                      {"Eng Productid(s)": "eng_product_ids"},
                      {"Arch": "arch"},
                      {"Username": "username"}]


def handle_attribute(attribute):
    """
    The function is used to handle the attribute name display in tool and in candlepin.
    For example, "Arch" is the display, but "arch" is used when to execute sql in db.
    :return: If select "Arch", then "arch" is returned.
    """
    for i in Attributes_dict_list:
        if i.keys()[0] == attribute:
            return i[attribute]


def advanced_search_str(attribute_select, attribute, attribute_text):
    if attribute_select == "contains":
        if attribute == "arch" or attribute == "eng_product_ids":
            search_attribute_text = search_arch_or_engproductid(attribute, attribute_text.lower())[0]
        else:
            search_attribute_text = '(fn.Lower(SkuEntry.{0}) % "%{1}%")'.format(attribute, attribute_text.lower())
    elif attribute_select == "does not contain":
        if attribute == "arch" or attribute == "eng_product_ids":
            search_attribute_text = search_arch_or_engproductid(attribute, attribute_text.lower())[1]
        else:
            search_attribute_text = '~(fn.Lower(SkuEntry.{0}) % "%{1}%")'.format(attribute, attribute_text.lower())
    elif attribute_select == "equals":
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) == "{1}")'.format(attribute, attribute_text.lower())
    elif attribute_select == "does not equal":
        search_attribute_text = '~(fn.Lower(SkuEntry.{0}) == "{1}")'.format(attribute, attribute_text.lower())
    elif attribute_select == "greater than":
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) > {1})'.format(attribute, attribute_text.lower())
    elif attribute_select == "less than":
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) < {1})'.format(attribute, attribute_text.lower())
    elif attribute_select == "is empty or null":
        search_attribute_text = '((fn.Lower(SkuEntry.{0}) == "-1") | (fn.Lower(SkuEntry.{0}) == "n/a"))'.format(attribute)
    elif attribute_select == "is not empty or null":
        search_attribute_text = '~((fn.Lower(SkuEntry.{0}) == "-1") | (fn.Lower(SkuEntry.{0}) == "n/a"))'.format(attribute)
    elif attribute_select == "is true":
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) == "1")'.format(attribute)
    elif attribute_select == "is not true":
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) == "0")'.format(attribute)
    else:
        # How to handle the blank select.
        search_attribute_text = '(fn.Lower(SkuEntry.{0}) % "%")'.format(attribute)
    return search_attribute_text


def advanced_search_default_choice(attribute1, choice1, attribute1_text, attribute2, choice2, attribute2_text,
                                   attribute3, choice3, attribute3_text, attribute4, choice4, attribute4_text):
    # Handle the default attribute choice.
    display_str = ""
    attribute_list = []
    attributes = [[attribute1, choice1, attribute1_text], [attribute2, choice2, attribute2_text],
                  [attribute3, choice3, attribute3_text], [attribute4, choice4, attribute4_text]]
    for attribute in attributes:
        if attribute[0] == "--Select Attribute--":
            attribute[0] = "id"
            display_str_tmp = ""
        else:
            display_str_tmp = "{0} - {1}: {2};".format(attribute[0], attribute[1], attribute[2])
        display_str += display_str_tmp
        attribute_list.append(attribute[0])
    return attribute_list, display_str


def search_arch_or_engproductid(attribute, input_datas):
    """
    The function is used to compose str that used in sql sentence of search Eng Product Id(s) or arch.
    Handle like this: (69,180,271) or (x86,x86_64,ppc64)
    :return: str
    """
    search_str = ""
    for input_data in input_datas.split(","):
        input_data = input_data.strip()
        if input_data != "":
            search_str_tmp = "(fn.Lower(SkuEntry.{0}) % '{1}%' |" \
                             "fn.Lower(SkuEntry.{0}) % '{1},%' |" \
                             "fn.Lower(SkuEntry.{0}) % '%,{1},%' |" \
                             "fn.Lower(SkuEntry.{0}) % '%,{1}') &".format(attribute, input_data)
        else:
            search_str_tmp = "(fn.Lower(SkuEntry.id) % '%') &"
        search_str += search_str_tmp
    contain_search_str = str(search_str + "&").replace("&&", "")
    not_contain_search_str = "~({0})".format(contain_search_str)

    return contain_search_str, not_contain_search_str

if __name__ == "__main__":
    for i in [i.keys()[0] for i in Attributes_dict_list]:
        print handle_attribute(i)




