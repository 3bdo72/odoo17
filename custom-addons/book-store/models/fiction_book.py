from odoo import models, fields, api


class FictionBook(models.Model):
    _name = "fiction"
    _description = "fiction book"

    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")
