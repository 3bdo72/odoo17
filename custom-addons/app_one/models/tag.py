from odoo import models, fields


class Tag(models.Model):
    _name = "tag"
    _description = "Des Tag"

    name = fields.Char(string="Name", required=True)
