# -*- coding: utf-8 -*-

import logging

from openerp.osv import fields, osv

_logger = logging.getLogger(__name__)

class product_template(osv.osv):
    _inherit = "product.template"

    def _get_product_multi_alias_join(self, cr, uid, ids, name, arg, context=None):
        res = {}
        for product in self.browse(cr, uid, ids, context=context):
            res[product.id] = '\n'.join([alias.name for alias in product.product_multi_alias_ids])
        return res

    _columns = {
        'product_multi_alias_ids': fields.one2many(
            'product.multi.alias', 'product_tmpl_id', 'Product Alias'
        ),
        'product_multi_alias_join': fields.function(
            _get_product_multi_alias_join, store=True, type='char', string='Alias'
        ),
    }


class product_multi_alias(osv.osv):
    _name = "product.multi.alias"
    _description = "Product Multi Alias"
    _order = "product_tmpl_id,sequence,id"

    _columns = {
        'name': fields.char('Alias', required=True),
        'sequence': fields.integer('Sequence'),
        'product_tmpl_id': fields.many2one('product.template', 'Product', 
            required=True, ondelete="cascade"),
    }

    _defaults = {
        'sequence': 1,
    }

    _sql_constraints = [
        ('unique_name', 'unique(product_tmpl_id,name)', 'Alias of product must be unique'),
    ]
