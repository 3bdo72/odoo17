from odoo import models, fields, api


class DramaBook(models.Model):
    _name = "drama"
    _description = "drama book"

    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")
