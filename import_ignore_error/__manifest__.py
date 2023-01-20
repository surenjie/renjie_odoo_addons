# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Import Ignore Error",
    'summary': "Model import data ignore error",
    'author': "renjie <i@renjie.me>",
    'website': "https://renjie.me",
    'support': 'i@renjie.me',
    'category': 'Extra Tools',
    'version': '1.0',
    'depends': ['base_import'],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'assets': {
        'web.assets_backend': [
            'import_ignore_error/static/src/js/import_ignore_error.js',
            'import_ignore_error/static/src/xml/import.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}