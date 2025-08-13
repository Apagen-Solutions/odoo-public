# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """This class inherits the model 'res.config.settings' and adds
     required fields"""
    _inherit = 'res.config.settings'

    def _get_account_manager_ids(self):
        """This function  gets all the records of 'res.users'  and
        it filters the 'res.users' records to select only those users
        who belong to the 'account.group_account_manager' group."""
        account_manager_ids = self.env['res.users'].search([
            ('groups_id', 'in', self.env.ref('account.group_account_manager').id)
        ])
        return [('id', 'in', account_manager_ids.ids)]

    payment_approval = fields.Boolean(
        string='Payment Approval',
        config_parameter='apg_account_payment_approval.payment_approval',
        help="Enable/disable payment approval to approve for payment if needed."
    )

    approval_user_id = fields.Many2one(
        'res.users',
        string="Payment Approving Person",
        required=False,
        domain=_get_account_manager_ids,
        config_parameter='apg_account_payment_approval.approval_user_id',
        help="Select the payment approving person."
    )

    approval_amount = fields.Float(
        string='Minimum Approval Amount',
        config_parameter='apg_account_payment_approval.approval_amount',
        help="If amount is 0.00, all the payments go through approval."
    )

    approval_currency_id = fields.Many2one(
        'res.currency',
        string='Approval Currency',
        config_parameter='apg_account_payment_approval.approval_currency_id',
        help="Converts the payment amount to this currency if chosen."
    )

