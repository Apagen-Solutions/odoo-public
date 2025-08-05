from odoo import api, fields, models


class SaleOrder(models.Model):
    """This class extends the base 'sale.order' model to introduce a
    new field, 'is_exchange',which allows users to manually apply an exchange
    rate for a transaction. When this option is enabled,users can specify the
    exchange rate through the 'rate' field."""
    _inherit = 'sale.order'

    is_exchange = fields.Boolean(string='Apply Manual Currency',
                                 help='Enable the boolean field to display '
                                      'rate field')
    rate = fields.Float(string='Rate', help='specify the currency rate',
                        compute='_compute_rate', readonly=False, store=True,
                        default=1)

    @api.depends('order_line.product_id')
    def _compute_rate(self):
        """Changing the unit price of product by changing the rate."""
        for rec in self:
            if len(rec.order_line) >= 1 and rec.is_exchange:
                rec.order_line[-1].price_unit = rec.order_line[
                                                    -1].product_id.list_price * rec.rate
