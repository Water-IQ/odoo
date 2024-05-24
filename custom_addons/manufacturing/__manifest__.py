# -*- coding: utf-8 -*-
{
    "name": "Custom Manufacturing",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "WaterIQ Technologies",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Manufacturing",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "mrp", "stock", "product"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "report/bom_report.xml",
    ],
    
    "installable": True,
    "application": False,
    "auto_install": True,
}
