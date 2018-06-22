# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class ResCompany(models.Model):
    _inherit = "res.company"

    def baidu_map_img(self, zoom=15, width=298, height=298):
        partner = self.partner_id
        return partner and partner.baidu_map_img(zoom=zoom, width=width, height=height) or None

    def baidu_map_link(self):
        partner = self.partner_id
        return partner and partner.baidu_map_link() or None
