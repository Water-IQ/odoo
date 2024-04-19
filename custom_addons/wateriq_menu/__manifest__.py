# -*- coding: utf-8 -*-
{
    "name": "wateriq_menu",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": """
Long description of module's purpose
    """,
    "author": "WaterIQ Technologies",
    "website": "https://www.wateriqtech.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["web", "mail"],
    # always loaded
    "data": [
        # "security/ir.model.access.csv",
        "views/layout_templates.xml",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "wateriq_menu/static/src/components/app_menu/side_menu.xml",
            "wateriq_menu/static/src/layout/style/layout_colors.scss",
            "wateriq_menu/static/src/components/app_menu/menu_order.css",
            "wateriq_menu/static/src/layout/style/layout_style.scss",
            "wateriq_menu/static/src/layout/style/sidebar.scss",
            "wateriq_menu/static/src/components/app_menu/search_apps.js",
        ],
        "web.assets_frontend": [
            "wateriq_menu/static/src/layout/style/login.scss",
        ],
    },
}
