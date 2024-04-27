from odoo import models, fields


# Book Model
class LibraryBook(models.Model):
    _name = "library.book"

    title = fields.Char(string="Book Title")
    author_id = fields.Many2one("library.author", string="Author")
    genre_ids = fields.Many2many("library.genre", string="Genres")
