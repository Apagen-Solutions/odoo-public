# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseProductHistoryLine(models.Model):
    """Purchase product history datas for product.product"""
    _name = 'purchase.product.history.line'
    _description = 'Product history line for product'

    product_history_id = fields.Many2one('product.product', string='Product',
                                         help='Name of the product')
    order_reference_id = fields.Many2one('purchase.order', string='Order',
                                         help='Purchase order reference of the'
                                              ' product')
    description = fields.Text(string='Description', help='Description of the'
                                                         ' product')
    price_unit = fields.Float(string='Unit Price', help='Unit price of the'
                                                        ' product')
    product_qty = fields.Float(string='Quantity', help='Product quantity')
    price_subtotal = fields.Float(string='Subtotal', help='Subtotal of the '
                                                          'product')
    vendor = fields.Many2one('res.partner', string="Vendor")
