from datetime import date
from odoo import models, fields, api
import re # for the regex
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(string="Reference", default="New", readonly=True)
    name = fields.Char(required=True, tracking=True, help="Name of the Patient")
    date_of_birth = fields.Date(tracking=True, help="Date of Birth")
    age = fields.Integer(tracking=True, compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], tracking=True, help="Gender of the Patient")
    active = fields.Boolean(default=True)
    address = fields.Text(help="Address of the Patient")
    phone = fields.Char(string='Phone', default='+20 ', required=True, help="Phone must start with +20", size=14, tracking=True)
    home_phone = fields.Char(string='Home Phone', default='03 ', required=True, help="Home Phone must start with 03", size=10, tracking=True)
    email = fields.Char(tracking=True)
    website = fields.Char(tracking=True)

    # Generate Reference Number when Patient is Created
    @api.model
    def create(self, vals):
        if vals.get('ref', 'New') == 'New':
            vals['ref'] = self.env['ir.sequence'].next_by_code('patient_ref') or 'New'
        return super(HospitalPatient, self).create(vals)


    # Validate Phone Numbers for +20 and 03
    @api.constrains('phone', 'home_phone')
    def _check_phone_numbers(self):
        phone_pattern = re.compile(r'^\+20 \d{10}$')
        home_phone_pattern = re.compile(r'^03 \d{7}$')
        
        for record in self:
            if record.phone and not phone_pattern.match(record.phone):
                raise ValidationError("Phone number must be in the format +20 XXXXXXXXXX (e.g., +20 1063097699).")
            if record.home_phone and not home_phone_pattern.match(record.home_phone):
                raise ValidationError("Home phone number must be in the format 03 XXXXXXX (e.g., 03 5411457).")

    # Compute Age from Date of Birth
    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.date_of_birth:
                birth_date = rec.date_of_birth
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                rec.age = age
            else:
                rec.age = 0

    def action_rainbow(self):
            return {
        'effect': {
            'fadeout': 'slow',
            'message': 'Congratulations, You are Rainbow Man',
            'type': 'rainbow_man',
        }
    }