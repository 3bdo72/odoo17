from odoo import models, fields, api

class PropertyHistory(models.Model):
    _name = 'property.history'
    _description = 'Property History'

    property_id = fields.Many2one('property', string="Property")
    user_id = fields.Many2one('res.users', string="User")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    reason = fields.Char()