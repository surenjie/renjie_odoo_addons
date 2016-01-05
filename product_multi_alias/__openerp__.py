# -*- coding: utf-8 -*-
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': "Product Multi Alias",
    'summary': 'Add more than one alias for your product',
    'description': """
Product Multi Alias
====================
Add more than one alias for your product
    """,
    'author': "renjie",
    'website': "http://renjie.me",
    'category': 'Sales',
    'version': '0.1',
    'depends': ['product'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_view.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
        'static/description/main_screenshot2.png',
        'static/description/main_screenshot3.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}