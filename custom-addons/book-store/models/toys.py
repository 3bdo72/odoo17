from odoo import models, fields


# Toys Model
class Toys(models.Model):
    _name = "toys"
    _description = "des toy"

    title = fields.Char(string="Toy Name")
