# -*- coding: utf-8 -*-

{
    'name': 'Purchase History Of Products',
    'version': '18.0.0.0',
    'category': 'Purchases',
    'summary': 'Easily view complete purchase history for any product in Form views',
    'description': """Users Can easily view complete purchase history for any product in Form views""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': "https://www.apagen.com",
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/product_template_views.xml',
        'views/product_product_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
