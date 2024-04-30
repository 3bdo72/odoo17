from odoo import models, fields


class LibraryCustomer(models.Model):
    _name = "library.customer"

    name = fields.Char(string="Customer Name")
    email = fields.Char(string="Email")
    password = fields.Char(string="Password")  # Add this line
    order_ids = fields.One2many("library.order", "customer_id", string="Orders")
