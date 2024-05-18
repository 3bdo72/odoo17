from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"  # we can find the name of the model that we want to inherit, from the url in the form or tree view page

    property_id = fields.Many2one("property")

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        print("inside the action confirm")  # our code
        return res

    def action_test_something(self):
        print("inside the action test something")