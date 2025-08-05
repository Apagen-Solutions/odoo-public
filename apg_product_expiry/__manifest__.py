
{
    'name': 'Lot and Serial Number Expiry Report',
    'version': '18.0.0.0',
    'category': 'Warehouse',
    'summary': 'Monitor and generate reports on the expiry dates of lot and serial numbers in inventory.',
    'description': """
    This module provides a comprehensive report on the expiry dates of products tracked by lot or serial numbers in Odoo.
""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'report/product_batch_report_reports.xml',
        'report/product_batch_report_templates.xml',
        'wizard/product_batch_report_views.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
