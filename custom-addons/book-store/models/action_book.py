from odoo import models, fields, api


class ActionBook(models.Model):
    _name = "action"
    _description = "action book"

    ref = fields.Char(default="New", readonly=True)
    name = fields.Char(string="Book Name")
    author = fields.Char(string="Author Name")
    category = fields.Char(string="Category", readonly=True, default="Action")

    amount = fields.Integer(string='Amount', required=True)
    currency = fields.Char(string='Currency', required=True)
    price = fields.Float(string='Price', required=True)

    def create_transaction_history(self):
        TransactionHistory = self.env['transaction.history']
        for book in self:
            TransactionHistory.create({
                'name': book.name,
                'author': book.author,
                'amount': book.amount,
                'currency': book.currency,
                'price': book.price,
                'category': book.category
            })

    @api.model
    def create(self, vals):
        """Override the create method to automatically create transaction history."""
        record = super(ActionBook, self).create(vals)
        record.create_transaction_history()
        return record

    def write(self, vals):
        """Override the write method to automatically create transaction history."""
        result = super(ActionBook, self).write(vals)
        self.create_transaction_history()
        return result



    @api.model
    def create(self, vals):
        res = super(ActionBook, self).create(vals)
        if res.ref == "New":
            res.ref = self.env["ir.sequence"].next_by_code("action_ref")
        return res