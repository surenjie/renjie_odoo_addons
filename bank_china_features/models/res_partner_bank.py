# -*- coding: utf-8 -*-

import json
import logging
from lxml import etree

from odoo import api, fields, models, _
from odoo.osv import expression

_logger = logging.getLogger(__name__)

class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    acc_name = fields.Char('Account Name', required=True)
    bank_info = fields.Char('Bank Info')
    is_company = fields.Boolean('Is Company', default=True)
    
    bank_id = fields.Many2one(required=True)
    partner_id = fields.Many2one(required=True)

    @api.multi
    @api.depends('acc_name', 'acc_number', 'bank_name')
    def name_get(self):
        result = []
        for bank in self:
            name = (bank.acc_name or '') + bank.acc_number + (bank.bank_name or '')
            result.append((bank.id, name))
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        domain = []
        if name:
            domain = [('sanitized_acc_number', 'like', '%' + name + '%')]
            domain = ['|'] + [('acc_name', operator, name)] + domain
            domain = ['|'] + [('bank_name', operator, name)] + domain
            if operator in expression.NEGATIVE_TERM_OPERATORS:
                domain = ['&'] + domain
        banks = self.search(domain + args, limit=limit)
        return banks.name_get()

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        if self.partner_id:
            self.acc_name = self.partner_id.name
        else:
            self.acc_name = None
        return {}

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(ResPartnerBank, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        default_partner_id = self._context.get('default_partner_id')
        if default_partner_id:
            doc = etree.XML(res['arch'])
            for node in doc.xpath("//field[@name='partner_id']"):
                node.set("readonly", "1")
                modifiers = json.loads(node.get("modifiers"))
                modifiers['readonly'] = True
                node.set("modifiers", json.dumps(modifiers))
            res['arch'] = etree.tostring(doc)
        return res
