__author__ = 'liusong'

import os
import json
from xml.dom.minidom import Document

FORMATS = ["csv", "json", "xml"]
test_data = [{'SKU': u'ESA0007', 'Instance Based Virt Multiplier': 'n/a', 'Virt Limit': 'n/a', 'Derived SKU': u'n/a', 'Support Level': u'Premium', 'Product Hierarchy: Product Line': u'BRMS / Rules', 'Management Enabled': False, 'Username': u'stage_esa_test', 'Product Family': u'JBoss', 'Product Hierarchy: Product Category': u'Subscriptions', 'RAM': 'n/a', 'Variant': u'BRMS', 'Product Hierarchy: Product Name': u'BRMS Platform', 'Support Type': u'L1-L3', 'Product Name': u'Enterprise Subscription for Red Hat JBoss BRMS', 'Multiplier': '1', 'Arch': u'n/a', 'Unlimited Product': True, 'Virt-only': False, 'Enabled Consumer Types': u'n/a', 'Socket(s)': 'n/a', 'Cloud Access Enabled': False, 'Required Consumer Type': u'n/a', 'Host Limited': False, 'Cores': 'n/a', 'JON Management': False, 'Eng Productid(s)': u'n/a', 'Multi Entitlement': False, 'VCPU': 'n/a', 'Stacking ID': u'n/a'}, {'SKU': u'MW0536563', 'Instance Based Virt Multiplier': 'n/a', 'Virt Limit': 'n/a', 'Derived SKU': u'n/a', 'Support Level': u'Standard', 'Product Hierarchy: Product Line': u'BRMS / Rules', 'Management Enabled': False, 'Username': u'stage_test_72_new', 'Product Family': u'JBoss', 'Product Hierarchy: Product Category': u'Subscriptions', 'RAM': 'n/a', 'Variant': u'Enterprise BRMS and BPM Suite', 'Product Hierarchy: Product Name': u'BRMS Platform', 'Support Type': u'Unrestricted L3', 'Product Name': u'Red Hat JBoss BRMS and BPM Suite with Management, 64 Core Standard, L3 Support Partner', 'Multiplier': '1', 'Arch': u'x86_64,ppc64,x86', 'Unlimited Product': True, 'Virt-only': False, 'Enabled Consumer Types': u'n/a', 'Socket(s)': 'n/a', 'Cloud Access Enabled': False, 'Required Consumer Type': u'n/a', 'Host Limited': False, 'Cores': '64', 'JON Management': True, 'Eng Productid(s)': u'183,185,239,301', 'Multi Entitlement': False, 'VCPU': 'n/a', 'Stacking ID': u'n/a'}]


def save_to(content, destination, name=None, extention="xml"):
    """
    To save the object in a local path
    :param content: str - The data need to save.
    :param destination: str - The directory to save the object to
    :param name: str - To rename the file name.
    :param extention: str - The format of file, support xml, csv, json.
    :return: The new location of the file or None
    """
    if not os.path.isdir(destination):
        raise IOError("'%s' is not a valid directory")
    obj_path = "{0}/{1}.{2}".format(destination, name, extention)
    with open(obj_path, "r") as f:
        new_file = f.write(content)
    return new_file if new_file else None


class XMLWriter(Document):
    def __init__(self):
        Document.__init__(self)

    def xml_generator(self, data):
        self.data = data
        # Set tag to "content"
        tag = self.createElement("content")
        self.appendChild(tag)

        # For every sku.
        for i in self.data:
            sku = self.createElement(i["SKU"])
            tag.appendChild(sku)
            # For every attribute in sku.
            for j in i.keys():
                attribute = self.createElement("attribute")
                sku.appendChild(attribute)
                name = self.createElement("name")
                attribute.appendChild(name)
                name_text = self.createTextNode(j)
                name.appendChild(name_text)
                # value
                value = self.createElement("value")
                attribute.appendChild(value)
                value_text = self.createTextNode(str(i[j]))
                value.appendChild(value_text)

        return self.toprettyxml(indent="    ")


class FileFormatConvert():
    def __init__(self, content):
        self.content = content

    def __get_header(self):
        return self.content[0].keys()

    def csv_format(self):
        # The first line of csv file.
        csv_str = str_header = ""
        for i in self.__get_header():
            str_header += "{0}{1}".format(i, ",")

        # Other lines.
        for i in self.content:
            s = ""
            for j in self.__get_header():
                s += "{0}{1}".format(i[j], ",")
            csv_str += "{0}\n".format(s)
        csv_str = "{0}\n{1}".format(str_header, csv_str)
        return csv_str

    def json_format(self):
        return json.dumps(self.content, indent=4).replace("[", "{").replace("]", "}")

    def xml_format(self):
        return XMLWriter().xml_generator(self.content)

    def save(self, file_format, file_path, file_name):
        content_str = name = ""
        if file_format == "csv":
            content_str = self.csv_format()
            name = "{0}.{1}".format(file_name, "csv")
        elif file_format == "json":
            content_str = self.json_format()
            name = "{0}.{1}".format(file_name, "json")
        elif file_format == "xml":
            name = "{0}.{1}".format(file_name, "xml")
        # Save the str into the file.
        name = file_path + name
        with open(name, "r") as f:
            f.write(content_str)

if __name__ == "__main__":
    f = FileFormatConvert(test_data)
    print "="*20
    print f.csv_format()
    print "="*20
    print f.json_format()
    print "="*20
    print f.xml_format()





