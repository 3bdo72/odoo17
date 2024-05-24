from odoo import models, fields, api

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    #Core Doctor Information:
    name = fields.Char(tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    x_avatar_image = fields.Binary()
    employee_id = fields.Many2one('hr.employee')
    department_id = fields.Many2one('hr.department')

    #Medical Credentials and Experience:
    specialization = fields.Selection([('cardiology', 'Cardiology'), ('orthopedics', 'Orthopedics'), ('neurology', 'Neurology'), ('oncology', 'Oncology'), ('emergency', 'Emergency'), ('other', 'Other')])
    license_number = fields.Char()
    years_of_experience = fields.Integer(tracking=True)
    education = fields.Char()
    certifications = fields.Char()

    #Contact and Availability:
    phone = fields.Char(tracking=True)
    email = fields.Char(tracking=True)
    website = fields.Char(tracking=True)
    availability = fields.Many2many('calender.event.slot')

    #Additional Considerations:
    biography = fields.Text()
    languages = fields.Many2many('res.lang')
    ratings_and_reviews = fields.Text()
    internal_notes = fields.Text()

    priority = fields.Selection([
        ('0', '0 Star'),
        ('1', '1 Stars'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars')], string="Priority")