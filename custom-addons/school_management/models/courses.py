from odoo import models, fields, api

class Courses(models.Model):
    _name = 'school_management.courses'
    _description = 'Courses'

    name = fields.Char(string='Course(s)', required=True)
    description = fields.Text(string='Description')
    duration = fields.Integer(string='Duration (in hours)')
    student_ids = fields.Many2many('school_management.school.student', string='Students')
