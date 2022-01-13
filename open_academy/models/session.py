from odoo import models, fields


class Session(models.Model):
    _name = 'session'
    _description = 'Session'
    course_id = fields.Many2one('course', required=True)
    instructor_id = fields.Many2one(
        'res.partner',
        domain="['|', ('is_instructor', '=', 'True'), ('category_id.name', 'like', 'Teacher'),]",
    )
    attendee_ids = fields.Many2many('res.partner')
    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float()
    number_seat = fields.Integer()
