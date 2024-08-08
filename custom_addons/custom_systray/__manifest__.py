# -*- coding: utf-8 -*-
{
    "name": "custom_systray",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "web",],
    # always loaded
    "data": [
    ],
    "assets": {
        "web.assets_backend": [
            "/custom_systray/static/src/xml/systray_icon.xml",
            "/custom_systray/static/src/js/systray_icon.js",
        ]
    },
}
