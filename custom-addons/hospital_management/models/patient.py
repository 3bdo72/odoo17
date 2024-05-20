from odoo import models, fields, api
import re # for the regex
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(string="Reference", default="New", readonly=True)
    name = fields.Char(required=True, tracking=True)
    age = fields.Integer(tracking=True)
    date_of_birth = fields.Date(tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True)
    active = fields.Boolean(default=True)
    address = fields.Text()
    phone = fields.Char(string='Phone', default='+20 ', required=True, help="Phone must start with +20", size=14, tracking=True)
    home_phone = fields.Char(string='Home Phone', default='03 ', required=True, help="Home Phone must start with 03", size=10, tracking=True)
    email = fields.Char(tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('ref', 'New') == 'New':
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient_ref') or 'New'
        return super(HospitalPatient, self).create(vals)

    # Another way of creating sequence number 
    # @api.model
    # def create(self, vals):
    #     res = super(HospitalPatient, self).create(vals)
    #     if res.ref == 'New':
    #         res.ref = self.env["ir.sequence"].next_by_code("patient_ref")
    #     return res

    @api.constrains('phone', 'home_phone')
    def _check_phone_numbers(self):
        phone_pattern = re.compile(r'^\+20 \d{10}$')
        home_phone_pattern = re.compile(r'^03 \d{7}$')
        
        for record in self:
            if record.phone and not phone_pattern.match(record.phone):
                raise ValidationError("Phone number must be in the format +20 XXXXXXXXXX (e.g., +20 1063097699).")
            if record.home_phone and not home_phone_pattern.match(record.home_phone):
                raise ValidationError("Home phone number must be in the format 03 XXXXXXX (e.g., 03 5411457).")


    class Fuction(models.Model):
        _name = 'hospital.patient.function'
        _description = 'Hospital Patient Function'

        name = fields.Char()