# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    china_icp_beian_info = fields.Char('China ICP BeiAn Info', related='website_id.china_icp_beian_info', readonly=False)

    baidu_analytics_key = fields.Char('Baidu Analytics Key', related='website_id.baidu_analytics_key', readonly=False)
    baidu_webmaster_push = fields.Boolean('Push web link to Baidu webmaster platform', related='website_id.baidu_webmaster_push', readonly=False)
    
    social_wechat = fields.Char('WeChat Account', related='website_id.social_wechat', readonly=False)
    social_qq = fields.Char('QQ Account', related='website_id.social_qq', readonly=False)
    social_weibo = fields.Char('Weibo Account', related='website_id.social_weibo', readonly=False)
    social_renren = fields.Char('Renren Account', related='website_id.social_renren', readonly=False)
