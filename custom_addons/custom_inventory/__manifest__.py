# -*- coding: utf-8 -*-
{
    "name": "custom_inventory",
    "summary": "Custom fields",
    "description": """

    """,
    "author": "WaterIQ Technologies",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "stock", "product", "purchase"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
}
