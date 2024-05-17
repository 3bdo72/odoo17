from odoo import api, fields, models

class ChangeStateWizard(models.TransientModel):
    _name = 'change.state.wizard'
    _description = 'Change State Wizard'

    property_id = fields.Many2one('property', string="Property")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
    ], string="New State", default = 'draft')

    reason = fields.Char()

    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.property_id.create_history_record('closed', self.state, self.reason)

