# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Product Multi Alias",
    'summary': 'Add more than one alias for your product',
    'author': "renjie <i@renjie.me>",
    'website': "https://renjie.me",
    'support': 'i@renjie.me',
    'category': 'Sales',
    'version': '0.2',
    'depends': ['product', 'sales_team'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
    'images': [
        'static/description/main_screenshot.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}