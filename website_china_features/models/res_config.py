# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class website_config_settings(models.TransientModel):
    _inherit = 'website.config.settings'

    china_icp_beian_info = fields.Char('China ICP BeiAn Info', related='website_id.china_icp_beian_info')

    baidu_analytics_key = fields.Char('Baidu Analytics Key', related='website_id.baidu_analytics_key')
    baidu_webmaster_push = fields.Boolean('Push web link to Baidu webmaster platform', related='website_id.baidu_webmaster_push')
    
    social_wechat = fields.Char('WeChat Account', related='website_id.social_wechat')
    social_qq = fields.Char('QQ Account', related='website_id.social_qq')
    social_weibo = fields.Char('Weibo Account', related='website_id.social_weibo')
    social_renren = fields.Char('Renren Account', related='website_id.social_renren')
