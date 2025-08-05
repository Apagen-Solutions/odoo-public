{
    'name': "Dynamic Product Code Based On Category",
    'summary': 'Automatically generate product codes dynamically based on selected product category',
    'description': """
    This module enables the automatic generation of product codes based on the selected product category.
    """,
    'author': 'Apagen Solution Pvt. Ltd',
    'website': 'https://www.apagen.com',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'icon': '/apg_dynamic_product_code/static/description/icon.png',
    'license': 'LGPL-3',
    'category': 'Productivity',
    'version': '18.0.0.0',

    'depends': ['product'],

    'data': [
        'views/product_category_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'demo': [],

    'installable': True,
    'application': True,
    'auto_install': False,

}
