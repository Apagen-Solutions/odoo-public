# -*- coding: utf-8 -*-


from odoo import fields, models


class ProductProduct(models.Model):
    """ProductProduct class represents to add purchase histories of
     the product"""
    _inherit = 'product.product'

    po_product_line_ids = fields.One2many('purchase.product.history.line',
                                          'product_history_id',
                                          string='Purchase History',
                                          compute='_compute_po_product_line_ids',
                                          help='Purchased product variant '
                                               'details')

    def _compute_po_product_line_ids(self):
        """Compute the purchase history lines. It will show all purchase order
         details of the particular product in product.template based on the
          limit and status."""
        self.po_product_line_ids = False
        status = self.env['ir.config_parameter'].sudo().get_param(
            'apg_purchase_product_history.status')
        limit = self.env['ir.config_parameter'].sudo().get_param(
            'apg_purchase_product_history.limit')
        if int(limit) >= 0 and status != False:
            state = ''
            if status == 'all':
                state = ('draft', 'sent', 'to approve', 'purchase', 'done',
                         'cancel')
            elif status == 'rfq':
                state = 'draft'
            elif status == 'purchase_order':
                state = ('purchase', 'done')
            order_line = self.env['purchase.order.line'].search([])
            if not limit:
                product_po_order_line = order_line.filtered(
                    lambda
                        l: l.product_id and l.product_id.id == self.id and l.state in state)
            else:
                product_po_order_line = order_line.search(
                    [('product_id', '=', self.id), ('state', 'in', state)],
                    limit=int(limit))
            self.env['purchase.product.history.line'].create([{
                'product_history_id': self.id,
                'order_reference_id': line.order_id.id,
                'description': line.name,
                'price_unit': line.price_unit,
                'product_qty': line.product_qty,
                'price_subtotal': line.price_subtotal,
                'vendor': line.partner_id,
            } for line in product_po_order_line] if product_po_order_line else [])
