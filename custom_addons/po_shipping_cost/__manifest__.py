# -*- coding: utf-8 -*-
{
    "name": "Custom PO Enhancements",
    "summary": "Adds custom fields and functionality to purchase orders",
    "description": """
        This module extends the functionality of purchase orders by adding a custom shipping cost field 
        and updating the total calculation.
    """,
    "author": "WaterIQ Technologies",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Purchases",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "purchase", "account"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": True,
}
