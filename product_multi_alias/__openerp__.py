# -*- coding: utf-8 -*-
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': "Product Multi Alias",
    'summary': '为您的产品添加多个别名',
    'description': "Add more than one alias for your product",
    'author': "renjie <i@renjie.me>",
    'website': "http://renjie.me",
    'category': 'Sales',
    'version': '0.2',
    'depends': ['product'],
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