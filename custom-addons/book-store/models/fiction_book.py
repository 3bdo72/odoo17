from odoo import models, fields, api


class FictionBook(models.Model):
    _name = "fiction"
    _description = "fiction book"

    ref = fields.Char(default = "New", readonly=True)
    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")

    @api.model
    def create(self, vals):
        res = super(FictionBook, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env["ir.sequence"].next_by_code("fiction_ref")
        return res