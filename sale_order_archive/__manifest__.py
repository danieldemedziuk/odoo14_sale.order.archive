# -*- coding: utf-8 -*-
{
    'name': "Sale order archive",
    'version': '1.0',
    'summary': "Add-on for sale",
    'description': "This is a module created for a recruiting assignment.",
    'author': "Daniel Demedziuk",
    'sequence': 90,
    'category': 'Tool',
    'depends': [
        'base',
        'sale',
    ],

    'data': [
        'security/ir.model.access.csv',
        'data/auto_archive.xml',
        'views/sale_order_archive_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
