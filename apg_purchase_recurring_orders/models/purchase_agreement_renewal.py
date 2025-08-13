# -*- coding: utf-8 -*-

from odoo import fields, models


class PurchaseAgreementRenewal(models.Model):
    """Renew purchase recurring agreement"""
    _name = 'purchase.agreement.renewal'
    _description = "Purchase Agreement Renewal"

    recurring_agreement_id = fields.Many2one('purchase.recurring.agreement',
                                             string='Agreement Reference',
                                             ondelete='cascade')
    date = fields.Datetime(string='Date', help="Date of the Renewal")
    comments = fields.Char(
        string='Comments', size=200, help='Renewal comments')
