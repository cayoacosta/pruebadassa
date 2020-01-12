# -*- coding: utf-8 -*-
##############################################################################
#                 @author 
#
##############################################################################

{
    'name': 'Dassa_Reports',
    'version': '12',
    'description': ''' That module Make in two Reports
                    in Customers Payments And One More Accounting 
                    Journal Entries 
    ''',
    'category': 'Accouting',
    'author': '',
    
    'depends': [
        'account'
    ],
    'data': [

        'reports/dassa_reports.xml',
        'reports/dassa_report_template.xml',
        'reports/dassa_poliza_de_template.xml',
        
    ],
    'application': False,
    'installable': True,
}
