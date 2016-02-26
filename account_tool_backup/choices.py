__author__ = "ftan"

from database import *

choices_list = []

for row in SkuEntry.select():
    choices_list.append(row.ph_product_name)

choices_list = list(set(choices_list))
choices_list.sort()

choices = []
for i in choices_list:
   t = (i, i)
   choices.append(t)
choices.insert(0, ("", "ALL Products"))

# The attributes. key is the displayed attribute name, value is the attribute name in candlepin.
Attributes_dict = [{"--Select Attribute--": "--Select Attribute--"},
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

attribute_choices = []
for i in [i.keys()[0] for i in Attributes_dict]:
    t = (i, i)
    attribute_choices.append(t)

# The search method.
select = ["", "contains", "does not contain", "equals", "does not equal", "greater than", "less than", "is empty or null",
          "is not empty or null", "is true", "is not true"]
select_choices = []
for i in select:
    t = (i, i)
    select_choices.append(t)


