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


class product_product(osv.osv):
    _inherit = "product.product"

    def search(self, cr, uid, args, offset=0, limit=None, order=None, context=None, count=False):
        if not context:
            context = {}
        if context.get('search_product_multi_alias'):
            if not args:
                args = []
            for index, arg in enumerate(args):
                if arg[0] == "name":
                    args.insert(index, ('product_multi_alias_join', arg[1], arg[2]))
                    args.insert(index, '|')
                    break
        return super(product_product, self).search(cr, uid, args, offset=offset, limit=limit, order=order, context=context, count=count)


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
