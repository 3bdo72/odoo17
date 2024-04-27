from odoo import models, fields, api


class ActionBook(models.Model):
    _name = "action"
    _description = "action book"

    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")
