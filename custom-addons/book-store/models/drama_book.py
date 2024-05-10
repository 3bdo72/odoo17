from odoo import models, fields, api


class DramaBook(models.Model):
    _name = "drama"
    _description = "drama book"

    ref = fields.Char(default="New", readonly=True)
    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")

    @api.model
    def create(self, vals):
        res = super(DramaBook, self).create(vals)
        if res.ref == "New":
            res.ref = self.env["ir.sequence"].next_by_code("drama_ref")
        return res