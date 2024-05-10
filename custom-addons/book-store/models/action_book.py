from odoo import models, fields, api


class ActionBook(models.Model):
    _name = "action"
    _description = "action book"

    ref = fields.Char(default="New", readonly=True)
    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")

    @api.model
    def create(self, vals):
        res = super(ActionBook, self).create(vals)
        if res.ref == "New":
            res.ref = self.env["ir.sequence"].next_by_code("action_ref")
        return res