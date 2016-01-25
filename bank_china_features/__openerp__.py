# -*- coding: utf-8 -*-
{
    'license': 'AGPL-3',
    'name': "Bank China Features",
    'summary': '中国特色银行账户信息',
    'description': "Bank account information with China features",
    'author': "renjie <i@renjie.me>",
    'website': "http://renjie.me",
    'category': 'Localization',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'data/res_bank.xml',
        'views/res_partner_bank.xml',
    ],
    'images': [
        'static/description/main_screenshot.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}