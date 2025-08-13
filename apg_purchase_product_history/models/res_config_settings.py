# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.exceptions import ValidationError


class ResConfigSettings(models.TransientModel):
    """ResConfigSettings class for adding the limit and status of products"""
    _inherit = 'res.config.settings'

    limit = fields.Integer(string='Limit', default=0,
                           config_parameter='apg_purchase_product_history.limit',
                           help='Specify the limit to show')
    status = fields.Selection(
        [('all', 'All'), ('rfq', 'RFQ'), ('purchase_order', 'Purchase Order')],
        string='Status',
        config_parameter='apg_purchase_product_history.status',
        help='Specify the status of the purchase order')

    def set_values(self):
        """inorder to set values in the settings"""
        res = super().set_values()
        self.env['ir.config_parameter'].set_param(
            'apg_purchase_product_history.limit',
            self.limit)
        self.env['ir.config_parameter'].set_param(
            'apg_purchase_product_history.status',
            self.status)
        if self.limit < 0:
            raise ValidationError("Limit cannot be less than 0")
        return res
