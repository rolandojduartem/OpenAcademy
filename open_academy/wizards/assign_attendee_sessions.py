from odoo import models, fields, Command


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assign.attendee.sessions'
    _description = 'Assign attendees'
    session_id = fields.Many2one('session', required=True)
    attendee_ids = fields.Many2many('res.partner')

    def save_this_session(self):
        self.session_id.write({'attendee_ids': [Command.link(attendee.id) for attendee in self.attendee_ids]})
