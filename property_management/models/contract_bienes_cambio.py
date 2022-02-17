from odoo import api, fields, models
from datetime import datetime


class RealEstateBienesCambio(models.Model):
    _name = 'real.estate.bienes.cambio'
    _description = 'Bienes de Cambio'

    def default_datetime(self):
        now = datetime.today()
        return now

    date_received = fields.Datetime(string='Fecha de Alta', default=default_datetime)

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Producto')
    
    contract_id = fields.Many2one(
        comodel_name='real.estate.contract',
        string='Contrato ID')

    description = fields.Text(string='Descripcion')

    cantidad = fields.Float('cantidad')

    uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string='Unidad'
    )

    precio = fields.Float('precio')
    ##################################################
    # ONCHANGES
    ##################################################