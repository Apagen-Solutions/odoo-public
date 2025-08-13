# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseTemplateHistoryLine(models.Model):
    """Purchase product history datas for product.template"""
    _name = 'purchase.template.history.line'
    _description = 'Purchase history line for template'

    history_id = fields.Many2one('product.template', string='Product',
                                 help='Name of the product variant')
    order_reference_id = fields.Many2one('purchase.order', string='Order',
                                         help='Purchase order reference of the'
                                              ' product')
    description = fields.Text(string='Description', help='Description of the'
                                                         ' product')
    price_unit = fields.Float(string='Unit Price', help='Unit price of the'
                                                        ' product')
    product_qty = fields.Float(string='Quantity', help='Product quantity')
    price_subtotal = fields.Float(string='Subtotal', help='Subtotal of the'
                                                          'product')
    vendor = fields.Many2one('res.partner', string="Vendor")
