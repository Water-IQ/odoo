# -*- coding: utf-8 -*-


{
    'name': 'odoo17 Tweak',
    'version': '24.03.27',
    'author': 'odooai.cn',
    'category': 'Extra Tools',
    'website': 'https://www.odooai.cn',
    'live_test_url': 'https://demo.odooapp.cn',
    'license': 'LGPL-3',
    'sequence': 2,
    'images': ['static/description/banner.gif'],
    'summary': """
    Ai as employee. 1 click Tweak odoo. 48 Functions odoo enhancement. for Customize, UI, Boost, Security, Development.
    Easy reset data, clear data, reset account chart, reset Demo data.
    For quick debug. Set brand,  Language Switcher all in one.
    """,
    'depends': [
        'app_common',
        'base_setup',
        'web',
        'mail',
    ],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/app_odoo_customize_views.xml',
        'views/app_theme_config_settings_views.xml',
        'views/res_config_settings_views.xml',
        'views/ir_views.xml',
        'views/ir_module_module_views.xml',
        'views/ir_translation_views.xml',
        'views/ir_module_addons_path_views.xml',
        'views/ir_ui_menu_views.xml',
        'views/ir_ui_view_views.xml',
        'views/ir_model_fields_views.xml',
        'views/ir_model_data_views.xml',
        'data/ir_config_parameter_data.xml',
        'data/ir_module_module_data.xml',
        'data/res_company_data.xml',
        'data/res_config_settings_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'app_odoo_customize/static/src/scss/app.scss',
            'app_odoo_customize/static/src/scss/ribbon.scss',
            'app_odoo_customize/static/src/scss/dialog.scss',
            'app_odoo_customize/static/src/js/user_menu.js',
            'app_odoo_customize/static/src/js/ribbon.js',
            'app_odoo_customize/static/src/js/dialog.js',
            'app_odoo_customize/static/src/webclient/*.js',
            'app_odoo_customize/static/src/webclient/user_menu.xml',
            'app_odoo_customize/static/src/xml/res_config_edition.xml',
        ],
    },
    'pre_init_hook': 'pre_init_hook',
    'installable': True,
    'application': True,
    'auto_install': False,

}
