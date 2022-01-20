from odoo import models, fields


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assign.attendee.sessions'
    _description = 'Assign attendees'
    session_id = fields.Many2one('session', required=True)
    attendee_ids = fields.Many2many('res.partner')
