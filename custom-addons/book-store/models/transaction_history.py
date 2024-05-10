from odoo import models, fields, api

class TransactionHistory(models.Model):
    _name = 'transaction.history'
    _description = 'Transaction History'

    name = fields.Char(string='Name', required=True)
    author = fields.Char(string="Author Name")
    amount = fields.Integer(string='Amount', required=True)
    currency = fields.Char(string='Currency', required=True)
    price = fields.Float(string='Price', required=True)
