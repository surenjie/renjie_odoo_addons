# -*- coding: utf-8 -*-

import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)

class website(models.Model):
    _inherit = "website"

    china_icp_beian_info = fields.Char('China ICP BeiAn Info')

    baidu_analytics_key = fields.Char('Baidu Analytics Key')
    baidu_webmaster_push = fields.Boolean('Baidu Webmaster Push')
    
    social_wechat = fields.Char('WeChat Account')
    social_qq = fields.Char('QQ Account')
    social_weibo = fields.Char('Weibo Account')
    social_renren = fields.Char('Renren Account')
