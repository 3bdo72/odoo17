from odoo import models, fields, api


# Order Model
class LibraryOrder(models.Model):
    _name = "library.order"

    customer_id = fields.Many2one("library.customer", string="Customer")
    name = fields.Char(string="Order Item Name")
    order_date = fields.Date(string="Order Date")
    total_amount = fields.Float(string="Total Amount")
    # You can add additional fields for order details (e.g., ordered books, quantities)
