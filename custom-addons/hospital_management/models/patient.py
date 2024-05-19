from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male')
    # doctor = fields.Many2one('hospital.doctor', ondelete='set null', index=True, null=True)