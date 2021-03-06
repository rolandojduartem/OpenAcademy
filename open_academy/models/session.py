from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta


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
    start_date = fields.Date(default=lambda self: fields.Date.today())
    end_date = fields.Date(compute='_compute_end_date')
    duration = fields.Integer(default=0)
    number_seat = fields.Integer(default=1, required=True)
    percentage_taken_seat = fields.Float(compute='_compute_percentage_taken_seat')
    count_attendee_ids = fields.Integer(compute="_compute_count_attendee_ids", store=True)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            record.end_date = record.start_date + timedelta(days=record.duration)

    @api.depends('attendee_ids', 'number_seat')
    def _compute_percentage_taken_seat(self):
        for record in self:
            if record.number_seat:
                record.percentage_taken_seat = (len(record.attendee_ids) / record.number_seat) * 100
            else:
                record.percentage_taken_seat = 0

    @api.depends('attendee_ids')
    def _compute_count_attendee_ids(self):
        for record in self:
            record.count_attendee_ids = len(record.attendee_ids)

    @api.onchange('attendee_ids', 'number_seat')
    def _onchange_percentage_taken_seat(self):
        title_message = None
        message = None
        if self.number_seat <= 0:
            title_message = 'Value not allowed!'
            message = 'Number seat can not be negative or zero'
        elif len(self.attendee_ids) > self.number_seat:
            title_message = 'This course is filled!'
            message = 'Attendee ids can not be greater than Number seat'
        if title_message and message:
            return {
                'warning': {
                    'title': title_message,
                    'message': message,
                }
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_on_attendee(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise ValidationError(_('Instructor can not be on attendee field'))

    @api.constrains('number_seat', 'attendee_ids')
    def _check_attendee_number_seat(self):
        for record in self:
            if record.number_seat < len(record.attendee_ids):
                raise ValidationError(_('The %s session can NOT have more attendees') % record.name)
