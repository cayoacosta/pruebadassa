# -*- coding: utf-8 -*-
##############################################################################
#                 @author IT Admin
#
##############################################################################

{
    'name': 'Reporte de Ventas del día',
    'version': '12.1',
    'description': ''' Reporte de facturas exportable a PDF o XLS
    ''',
    'category': 'Stock',
    'author': 'IT Admin',
    'website': 'http://www.itadmin.com.mx',
    'depends': [
        'base','stock', 'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/invoice_report_wizard.xml',
        'report/invoice_report.xml',
    ],
    'application': False,
    'installable': True,
}
