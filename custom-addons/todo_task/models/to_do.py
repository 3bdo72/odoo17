from odoo import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Task Name')
    assign_to = fields.Many2one('res.partner', string='Assigned To')
    description = fields.Text('Description')
    due_date = fields.Date('Due Date')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Task Status')

    def action_new(self):
        for rec in self:
            rec.state = "new"

    def action_progress(self):
        for rec in self:
            rec.state = "in_progress"

    def action_completed(self):
        for rec in self:
            rec.state = "completed"
