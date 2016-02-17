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

Header = ['arch',
          'cloud_access_enabled',
          'cores',
          'derived_sku',
          'enabled_consumer_types',
          'host_limited',
          'instance_multiplier',
          'jon_management',
          'management_enabled',
          'multi-entitlement',
          'multiplier',
          'name',
          'ph_category',
          'ph_product_line',
          'ph_product_name',
          'product_family',
          'ram',
          'requires_consumer_type',
          'sockets',
          'stacking_id',
          'support_level',
          'support_type',
          'unlimited_product',
          'variant',
          'vcpu',
          'virt_limit',
          'virt_only']

attribute_choices = []
for i in Header:
    t = (i, i)
    attribute_choices.append(t)

select = ["contains", "does not contain", "equals", "does not equal", "greater than", "less than", "is empty or null",
          "is not empty or null"]
select_choices = []
for i in select:
    t = (i, i)
    select_choices.append(t)


