from odoo import models, fields, api


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
    number_seat = fields.Integer(default=1, required=True)
    percentage_taken_seat = fields.Float(compute='_calculate_percentage_taken_seat')

    @api.depends('attendee_ids', 'number_seat')
    def _calculate_percentage_taken_seat(self):
        for record in self:
            record.percentage_taken_seat = (len(record.attendee_ids) / record.number_seat) * 100 if record.number_seat > 0 else 0

    @api.onchange('attendee_ids', 'number_seat')
    def _onchange_percentage_taken_seat(self):
        if self.number_seat <= 0:
            return {
                'warning':{
                    'title': 'Value not allowed!',
                    'message': 'Number seat can not be negative or zero'
                }
            }
        elif len(self.attendee_ids) > self.number_seat:
            return {
                'warning': {
                    'title': 'This course is filled!',
                    'message': 'Attendee ids can not be greater than Number seat',
                }
            }
