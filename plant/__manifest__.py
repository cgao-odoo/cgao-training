# -*- coding: utf-8 -*-
{
    'name': "Plant Nursery",
    'version': "1.0",

    'summary': """
        Plant Management
    """,

    'description': """
        Nursery Module
    """,

    'author': "cgao",
    'website': "http://www.odoo.com",
    
    'depends': ['base'],
    
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/data.xml',
    ],
}