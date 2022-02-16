from odoo import models, fields, api


class RealEstatePropertyIcc(models.Model):
    _name = 'real.estate.property.icc'
    _description = 'Real Estate Property ICC'

    icc_date = fields.Date(string='Fecha de ICC', help='Solo se puede tener una carga por mes.', required=True)
    icc_percent = fields.Float(string='Porcentaje', help='Porcentaje de este ICC', required=True)