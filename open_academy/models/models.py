# -*- coding: utf-8 -*-

from odoo import models, fields


class Course(models.Model):
     _name = 'course.model'
     title = fields.Char(required = True)
     description = fields.Char()
