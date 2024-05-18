from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_do_something(self):
        print(self, 'I am doing something')