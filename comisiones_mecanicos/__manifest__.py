# -*- coding: utf-8 -*-
{
    'name': "Comisiones_mecanicos",

    'summary': """
        Added new menu for taller in report
        Filter all Ordenes de reparacion” documents within selected dates and that are in state = “Cerrado”
        
        """,

    'description': """

    """,

    'author': "IT Admin",
    'website': "www.itadmin.com",
    'category': '',
    'version': '12.4',
    'depends': [
        'taller'
        ],
    'data': [
        'views/menu_tab.xml',
        'security/ir.model.access.csv',
        'wizard/comisiones_a_mecancios_view.xml',
        'reports/comisiones_mecanicos_report.xml',
    ],

}
