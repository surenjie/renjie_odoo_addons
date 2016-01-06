# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class website(osv.osv):
    _inherit = "website"
    _columns = {
        'china_icp_beian_info': fields.char('China ICP BeiAn Info'),

        'baidu_analytics_key': fields.char('Baidu Analytics Key'),
        'baidu_webmaster_push': fields.boolean('Baidu Webmaster Push'),
        
        'social_wechat': fields.char('WeChat Account'),
        'social_qq': fields.char('QQ Account'),
        'social_weibo': fields.char('Weibo Account'),
        'social_renren': fields.char('Renren Account'),
    }
