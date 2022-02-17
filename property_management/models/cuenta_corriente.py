from odoo import models, fields, api


class CuentaCorriente(models.Model):
    _name = 'real.estate.cuenta.corriente'
    _description = 'Property Account Debt'

    fecha = fields.Date(string='Fecha')
    numero_pago = fields.Char(string='Numero de Pago')
    monto = fields.Float(string="Monto")
    saldo_total = fields.Float(string="Saldo Total")