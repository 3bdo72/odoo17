from odoo import models, fields, api


# Author Model
class LibraryAuthor(models.Model):
    _name = "library.author"

    name = fields.Char(string="Author Name")
    biography = fields.Text(string="Biography")
