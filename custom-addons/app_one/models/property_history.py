from odoo import models, fields, api

class PropertyHistory(models.Model):
    _name = 'property.history'
    _description = 'Property History'

    property_id = fields.Many2one('property', string="Property")
    user_id = fields.Many2one('res.users', string="User")
    old_state = fields.Char(string="Old State")
    new_state = fields.Char(string="New State")
    reason = fields.Char()
    
    bathroom_history_line_ids = fields.One2many('property.bathroom.line.history', 'bath_property_id', string="Bathrooms")
    bedroom_history_line_ids = fields.One2many('property.bedroom.line.history', 'bed_property_id', string="Bedrooms")


class BathroomLine(models.Model):
    _name = "property.bathroom.line.history"
    _description = "Property Bathroom Line"

    bath_property_id = fields.Many2one("property.history")
    area = fields.Float()
    description = fields.Char()

class BedroomLine(models.Model):
    _name = "property.bedroom.line.history"
    _description = "Property Bedroom Line"

    bed_property_id = fields.Many2one("property.history")
    area = fields.Float()
    description = fields.Char()