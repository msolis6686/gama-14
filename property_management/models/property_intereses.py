from odoo import models, fields, api


class RealEstatePropertyInterest(models.Model):
    _name = 'real.estate.property.interest'
    _description = 'Real Estate Property Intereses'

    interest_date = fields.Date(string='Fecha del Alta del Interes', required=True)
    interest_monthly_type = fields.Integer(string='Meses', required=True)
    interest_rate = fields.Float(string='Porcentaje de Interes', required=True)