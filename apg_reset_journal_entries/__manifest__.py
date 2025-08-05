# -*- coding: utf-8 -*-

{
    'name': 'Reset Journal Entries',
    'version': '18.0.0.0',
    'category': 'Accounting',
    'summary': 'Allows resetting of posted journal entries to draft for correction',
    'description': """
    This module enables authorized users to reset posted journal entries back to draft state in Odoo, allowing corrections or updates before final posting.
    """,
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com',
    'depends': ['account'],
    'data': [
        'data/ir_action_server_data.xml',
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False
}
