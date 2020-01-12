# -*- coding: utf-8 -*-#
from odoo import api,fields,models
from odoo.exceptions import Warning

class ComisionesAMecancios(models.TransientModel):
    _name ="comisiones.a.mecancios"
    
    date_start=fields.Date("Periodo")
    date_end= fields.Date('Al')
    
    @api.multi
    def print_report(self):
        self.ensure_one()
        
        find_record = [('fecha','>=',self.date_start),('fecha','<=',self.date_end),('state','=','Cerrada')]    
        selected_record = self.env['ordenes.de.reparacion'].search(find_record)
        if not selected_record:
            raise Warning("No any ordenes de reparacion found for given date range with status Cerrada.")
        return self.env.ref('comisiones_mecanicos.comisiones_mecanicos_reports_main').with_context(from_transient_model=True).report_action(selected_record)
                
        