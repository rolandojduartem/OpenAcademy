from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'
    responsible_id = fields.Many2one('res.users')
    title = fields.Char(required=True)
    description = fields.Text()
