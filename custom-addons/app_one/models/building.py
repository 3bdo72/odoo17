from odoo import models, fields

class Building(models.Model):
    _name = "building"
    _description = "Building"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _rec_name = "code"

    num = fields.Integer(string="Number")
    code = fields.Char(string="Code")
    description = fields.Text(string="Description")
    active = fields.Boolean(string="Active", default=True, invisible=True)