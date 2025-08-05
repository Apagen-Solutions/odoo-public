from odoo import api, fields, models


class AccountPayment(models.Model):
    _inherit = 'account.payment'

    is_exchange = fields.Boolean(
        string="Apply Manual Exchange",
        help="Check this box if you want to manually apply an exchange rate for this payment."
    )

    rate = fields.Float(
        string="Exchange Rate",
        help="Specify the manual exchange rate.",
        default=1.0,
        
        readonly=False,
        store=True
    )
    amount = fields.Monetary(currency_field='currency_id',store=True ,compute='compute_rate',)
    # @api.onchange('is_exchange', 'rate', 'amount', 'currency_id', 'company_id')
    @api.onchange('rate')
    def compute_rate(self):
        for rec in self:
            if rec.is_exchange and rec.currency_id and rec.company_id:
                company_currency = rec.company_id.currency_id
                if rec.currency_id != company_currency:
                    rec.amount = rec.amount * rec.rate
