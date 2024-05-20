from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    #Core Doctor Information:
    name = fields.Char()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    image = fields.Image()
    employee_id = fields.Many2one('hr.employee')
    department_id = fields.Many2one('hr.department')

    #Medical Credentials and Experience:
    specialization = fields.Selection([('cardiology', 'Cardiology'), ('orthopedics', 'Orthopedics'), ('neurology', 'Neurology'), ('oncology', 'Oncology'), ('emergency', 'Emergency'), ('other', 'Other')])
    license_number = fields.Char()
    years_of_experience = fields.Integer()
    education = fields.Char()
    certifications = fields.Char()

    #Contact and Availability:
    phone = fields.Char()
    email = fields.Char()
    availability = fields.Many2many('calender.event.slot')

    #Additional Considerations:
    biography = fields.Text()
    languages = fields.Many2many('res.lang')
    ratings_and_reviews = fields.Text()
    internal_notes = fields.Text()