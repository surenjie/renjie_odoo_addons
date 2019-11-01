# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class product_template(models.Model):
    _inherit = "product.template"

    product_multi_alias_ids = fields.One2many('product.multi.alias', 'product_tmpl_id', string='Product Alias')
    product_multi_alias_join = fields.Char(compute='_compute_product_multi_alias_join', store=True, string='Alias')

    @api.depends('product_multi_alias_ids.name')
    def _compute_product_multi_alias_join(self):
        for rec in self:
            rec.product_multi_alias_join = '\n'.join([alias.name for alias in rec.product_multi_alias_ids])


class product_product(models.Model):
    _inherit = "product.product"

    @api.model
    def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
        if self._context.get('search_product_multi_alias'):
            if not args:
                args = []
            for index, arg in enumerate(args):
                if arg[0] == "name":
                    args.insert(index, ('product_multi_alias_join', arg[1], arg[2]))
                    args.insert(index, '|')
                    break
        return super(product_product, self)._search(args, offset=offset, limit=limit, order=order, count=count, access_rights_uid=access_rights_uid)


class product_multi_alias(models.Model):
    _name = "product.multi.alias"
    _description = "Product Multi Alias"
    _order = "product_tmpl_id,sequence,id"

    name = fields.Char('Alias', required=True)
    sequence = fields.Integer('Sequence', default=1)
    product_tmpl_id = fields.Many2one('product.template', 'Product', required=True, ondelete="cascade")

    _sql_constraints = [
        ('unique_name', 'unique(product_tmpl_id,name)', 'Alias of product must be unique'),
    ]
