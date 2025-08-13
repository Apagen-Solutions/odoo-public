# -*- coding: utf-8 -*-

{
    'name': 'Recurring Purchase Orders',
    'version': '18.0.0.0',
    'category': 'Inventory,Purchases',
    'summary': """Automate the creation of recurring purchase orders to save time and ensure timely stock replenishment in Odoo.""",
    'description': """This module Helps to Automate the creation of recurring purchase orders to save time and ensure timely stock replenishment in Odoo.""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['purchase'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'data/ir_sequence_data.xml',
        'wizard/renew_wizard_views.xml',
        'views/recurring_orders_views.xml',
        'views/purchase_order_views.xml',
        'views/res_partner_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
