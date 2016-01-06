# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class website_config_settings(osv.osv_memory):
    _inherit = 'website.config.settings'
    _columns = {
        'china_icp_beian_info': fields.related('website_id', 'china_icp_beian_info', type="char", string='China ICP BeiAn Info'),

        'baidu_analytics_key': fields.related('website_id', 'baidu_analytics_key', type="char", string='Baidu Analytics Key'),
        'baidu_webmaster_push': fields.related('website_id', 'baidu_webmaster_push', type="boolean", string='Push web link to Baidu webmaster platform'),
        
        'social_wechat': fields.related('website_id', 'social_wechat', type="char", string='WeChat Account'),
        'social_qq': fields.related('website_id', 'social_qq', type="char", string='QQ Account'),
        'social_weibo': fields.related('website_id', 'social_weibo', type="char", string='Weibo Account'),
        'social_renren': fields.related('website_id', 'social_renren', type="char", string='Renren Account'),
    }
