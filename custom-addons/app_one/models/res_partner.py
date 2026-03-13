from odoo import models, fields, api
class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_property_owner = fields.Boolean(string="Is Property Owner")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
