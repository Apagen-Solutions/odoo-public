# -*- coding: utf-8 -*-

{
    'name': 'Payment Approval Process',
    'version': '18.0.0.0',
    'category': 'Accounting',
    'summary': """ The Account Payment Approval module adds an extra layer of control to your payment process in Odoo by introducing an approval workflow for outgoing payments.""",
    'description': """The Account Payment Approval module adds an extra layer of control to your payment process in Odoo by introducing an approval workflow for outgoing payments. """,
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': "https://www.apagen.com",
    'depends': ['base','account'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/account_payment_views.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
