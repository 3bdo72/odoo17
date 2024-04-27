from odoo import models, fields


# Genre Model
class LibraryGenre(models.Model):
    _name = "library.genre"

    name = fields.Char(string="Genre Name")
    book_ids = fields.Many2many("library.book", string="Books")
