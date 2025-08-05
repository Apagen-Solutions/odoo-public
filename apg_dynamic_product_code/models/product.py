# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = 'product.template'


    @api.model_create_multi
    def create(self, vals):
        res = super().create(vals)
        if res.categ_id.sequence_id:
            res.write({
                'default_code' : res.categ_id.sequence_id.next_by_id()
            })
        return res

    def write(self, vals):
        result = super(ProductTemplate, self).write(vals)
        for rec in self:
            if not rec.default_code:
                if rec.categ_id.sequence_id:
                    rec.write({
                        'default_code' : rec.categ_id.sequence_id.next_by_id()
                    })
        return result

