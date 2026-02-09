# -*- coding: utf-8 -*-
{
    'name': 'Eskola',
    'version': '1.0',
    'summary': 'Eskolaren kudeaketa',
    'description': 'Eskola modulua: ikasleak, irakasleak eta klaseak',
    'author': 'Zure Izena',
    'category': 'Education',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/eskola_views.xml',
        'views/eskola_menu.xml',
    ],
    'installable': True,
    'application': True,
}
