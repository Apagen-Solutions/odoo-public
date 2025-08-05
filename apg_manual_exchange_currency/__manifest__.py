{
    'name': "Manual Currency Exchange Rate",
    'version': '18.0.0.0',
    'category': 'Accounting',
    'summary': 'Allow users to manually input exchange rates for currency transactions in accounting.',
    'description': """
    This module allows users to manually input currency exchange rates during accounting transactions, providing flexibility and control over currency conversions.""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['base', 'purchase', 'sale_management', 'account'],
    'data': [
        'views/account_move_views.xml',
        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',
        'views/account_payment_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
