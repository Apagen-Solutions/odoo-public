# -*- coding: utf-8 -*-

{
    'name': 'Export Product Stock in Excel',
    'version': '18.0.0.0',
    'summary': 'Easily export real-time product stock data to Excel with a single click.',
    'description': 'The Export Product Stock in Excel module enables users to quickly export detailed inventory data into an Excel spreadsheet directly from the Odoo backend. ',
    'category': 'Warehouse',
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'depends': [
        'sale_management',
        'stock',
        'purchase',
    ],
    'website': 'https://www.apagen',
    'data': [
        'security/ir.model.access.csv',
        'wizard/stock_report_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'apg_export_stock_xls/static/src/js/action_manager.js',
        ],
    },
    'images': ['static/description/banner.jpg'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'auto_install': False,
}
