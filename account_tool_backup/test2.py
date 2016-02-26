__author__ = 'liusong'

from utils import *

sku_matrix = []

# arch
for row in SkuEntry.select().where((~((fn.Lower(SkuEntry.eng_product_ids) % '69,%' |fn.Lower(SkuEntry.eng_product_ids) % '%,69,%' |fn.Lower(SkuEntry.eng_product_ids) % '%,69'))) & (fn.Lower(SkuEntry.arch) % 'x86,%' |fn.Lower(SkuEntry.arch) % '%,x86,%' |fn.Lower(SkuEntry.arch) % '%,x86') & (~((fn.Lower(SkuEntry.arch) % 'x86_64,%' |fn.Lower(SkuEntry.arch) % '%,x86_64,%' |fn.Lower(SkuEntry.arch) % '%,x86_64'))) & (fn.Lower(SkuEntry.id) % "%")):
    meta = {}
    meta["SKU"] = row.id
    meta['Arch'] = row.arch
    meta['cloud_access_enabled'] = row.cloud_access_enabled
    sku_matrix.append(meta)

print sku_matrix
print len(sku_matrix)


SearchMethods_dict = [{"--Select Attribute--": "--Select Attribute--"},
                      {"SKU": "id"},
                      {"Product Hierarchy: Product Category": "ph_category"},
                      {"Product Hierarchy: Product Line": "ph_category"},
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

print "*"*20
print SearchMethods_dict.keys()
