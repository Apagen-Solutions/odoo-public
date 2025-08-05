# -*- coding: utf-8 -*-
{
    'name': "Product Secondary Unit of Measure",
    'version': '18.0.0.0',
    'category': "Extra Tools",
    'summary': "Creates a new column or field for secondary UoM. ",
    'description': """
       
        Secondary Product UOM Odoo App helps users to managing or converting the secondary unit of measure of the product from a primary unit of measure and vice versa. User can add secondary quantity and secondary unit of measure in sale order, stock picking and purchase order.
    
    """,
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['base', 'sale_management', 'stock', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/stock_quant_view.xml',
        'views/sale_order_line_view.xml',
        'views/purchase_order_line_view.xml',
        'views/stock_move_view.xml',
    ],

    'images': [
        'static/description/banner.jpg',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
