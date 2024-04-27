from odoo import fields, models

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book Information'

    # Other Book fields (name, author_id, publication_date, etc.)

    category_ids = fields.Many2many(
        comodel_name='library.category', 
        string='Categories')  # Many2many
    member_id = fields.Many2one(
        comodel_name='library.member', string='Checked Out By')  # Many2one
    reviewed_by = fields.One2many(
        comodel_name='library.review', 
        inverse_name='book_id', 
        string='Reviews')  # One2many


class Category(models.Model):
    _name = 'library.category'
    _description = 'Book Category'

    name = fields.Char(string='Category Name', required=True)
    # Add other relevant category fields



class Review(models.Model):
    _name = 'library.review'
    _description = 'Book Review'

    book_id = fields.Many2one(
        comodel_name='library.book', 
        string='Book', 
        ondelete='cascade')  # Essential for data integrity
    content = fields.Text(string='Review Content')
    rating = fields.Integer(string='Rating')  # Example field
    # Add other relevant review fields (e.g., author_id)
