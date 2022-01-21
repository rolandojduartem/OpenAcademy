from odoo import models, fields, Command


class AssignAttendeeSessions(models.TransientModel):
    _name = 'assign.attendee.sessions'
    _description = 'Assign attendees'
    session_ids = fields.Many2many('session', required=True)
    attendee_ids = fields.Many2many('res.partner')

    def action_register_attendees_to_sessions(self):
        updated_records = [Command.link(attendee.id) for attendee in self.attendee_ids]
        for record in self.session_ids:
            record.write({'attendee_ids': updated_records})
