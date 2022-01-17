from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'
    _sql_constraints = [
        ('check_title_description', 'CHECK(title<>description)', "Title can not be equal to description"),
        ('title_unique', 'UNIQUE(title)', "The course's title exists"),
    ]
    session_ids = fields.One2many('session', 'course_id')
    responsible_id = fields.Many2one('res.users')
    title = fields.Char(required=True)
    description = fields.Text()
