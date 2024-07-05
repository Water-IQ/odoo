# -*- coding: utf-8 -*-
{
    'name': "grid_view",

    'summary': "",

    'description': """

    """,

    'author': "WaterIQ Tech.",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Custom',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'grid_view/static/src/js/*.js',
            'grid_view/static/src/views/*.xml',
        ],
    },
}

