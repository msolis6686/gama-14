from odoo import models, fields, api


class RealEstatePropertyHistorico(models.Model):
    _name = 'real.estate.property.historico'
    _description = 'Real Estate Property Historico'

    operation = fields.Char(string='Operacion')
    description = fields.Text(string='Descripcion')
    reg_date = fields.Datetime(string='Fecha y Hora')