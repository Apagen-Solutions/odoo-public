from odoo import api, fields, models


class PurchaseOrder(models.Model):
    """This class extends the base 'purchase.order' model to introduce a
    new field, 'is_exchange',which allows users to manually apply an exchange
    rate for a transaction. When this option is enabled, users can specify
    the exchange rate through the 'rate' field."""
    _inherit = 'purchase.order'

    is_exchange = fields.Boolean(string='Apply Manual Currency',
                                 help='Check this box if you want to manually'
                                      'apply an exchange rate for this '
                                      'transaction.')
    rate = fields.Float(string='Rate', help='specify the rate', compute='_compute_rate', readonly=False, store=True,
                        default=1)

    @api.depends('order_line.product_id')
    def _compute_rate(self):
        """Changing the unit price of product by changing the rate."""
        for rec in self:
            if len(rec.order_line) >= 1 and rec.is_exchange:
                rec.order_line[-1].price_unit = rec.order_line[
                                                    -1].product_id.standard_price * rec.rate
