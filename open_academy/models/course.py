from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _rec_name = 'title'
    _description = 'Course'
    _sql_constraints = [
        ('check_title_description', 'CHECK(title<>description)', "Title can not be equal to description"),
        ('title_unique', 'UNIQUE(title)', "The course's title exists"),
    ]
    session_ids = fields.One2many('session', 'course_id')
    responsible_id = fields.Many2one('res.users')
    title = fields.Char(required=True, copy=False)
    description = fields.Text()

    def copy_data(self, default=None):
        res = super().copy_data(default=default)
        for copy_values in res:
            copy_values['title'] = 'Copy of [%s]' % self.title
        return res
