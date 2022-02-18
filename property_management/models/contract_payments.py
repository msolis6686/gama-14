from odoo import api, fields, models
from datetime import datetime


class RealEstatePayments(models.Model):
    _name = 'real.estate.payments'
    _description = 'Pagos de Contrato'
    
    contract_id = fields.Many2one(
        comodel_name='real.estate.contract',
        string='Contrato ID')
    
    payment_id = fields.Many2one('account.payment', string='Pagos')
    
class AccountPayment(models.Model):
    _inherit = 'account.payment'
    _description = 'Inherit de account payment para one2many de pagos'

    def context_get_partner(self):
        print('contexto')
        partner_id = self.env.context.get('contract_partner_id')
        print(partner_id)
        if partner_id:
            return partner_id
    
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Customer/Vendor",
        store=True, readonly=False, ondelete='restrict',
        compute='_compute_partner_id',
        domain="['|', ('parent_id','=', False), ('is_company','=', True)]",
        check_company=True,
        default=context_get_partner)

    contract_o2m_rel = fields.Many2one(
        comodel_name='real.estate.contract',
        string='Contrato/Pago'
    )