from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'
    is_instructor = fields.Boolean()
    session_partner = fields.Many2many('session')
