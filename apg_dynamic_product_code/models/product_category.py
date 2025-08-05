# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'


    product_sequence_id = fields.Many2one('ir.sequence', copy=False)
    sequence_id = fields.Many2one('ir.sequence', string='Item Code Sequence')
    item_code = fields.Char(string="Prefix Item Code", required=False)

    def open_sequence_changes(self):
        action = self.env["ir.actions.actions"]._for_xml_id("apg_dynamic_product_code.action_category_sequence")
            
        context = {
            'default_category_id':self.id,
        }
        if self.product_sequence_id:
            context['default_prefix'] = self.product_sequence_id.prefix
            context['default_padding'] = self.product_sequence_id.padding
        action['context'] = context
        return action

    def write(self, vals):
        result = super(ProductCategory, self).write(vals)
        # if not self.sequence_id:
        if 'item_code' in vals:
            item_code = "product.category" + "." + self.item_code
            item_sequence = self.env['ir.sequence'].create({
                'name': self.name,
                'code': item_code,
                'prefix': self.item_code,
                'implementation': 'no_gap',
                'padding': 5,
                'number_next': 1,
            })
            self.sequence_id = item_sequence.id
        return result
