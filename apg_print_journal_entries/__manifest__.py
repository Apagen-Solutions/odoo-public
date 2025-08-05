# -*- coding: utf-8 -*-
{
    'name': 'Print Journal Entries Report in Odoo',
    'version': '18.0.0.0',
    'category': 'Accounting',
    'license': 'LGPL-3',
    'summary': 'Generate a detailed PDF report of all journal entries for printing and review',
    'description': """
    This module enables users to print journal entries as professionally structured PDF reports directly from Odoo.""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['base', 'account'],
    'data': [
        'report/report_journal_entries.xml',
        'report/report_journal_entries_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'installable': True,
    'auto_install': False,
}
