import datetime
from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    est_time = fields.Float(string='Estimated Time')
    line_ids = fields.One2many('todo.timesheet.line', 'task_id')
    active = fields.Boolean(string='Active', default=True)
    total_hours = fields.Float(compute='_compute_total')
    is_late = fields.Boolean(readonly=True)
    
    @api.depends('line_ids.duration', 'est_time')
    def _compute_total(self):
        for rec in self:
            total = 0.0
            for line in rec.line_ids:
                total += line.duration
            rec.total_hours = total
            if rec.total_hours > rec.est_time:
                raise ValidationError('Total of Time Sheets hours more than Estimated time !!')

    def action_new(self):
        for rec in self:
            rec.state = "new"

    def action_progress(self):
        for rec in self:
            rec.state = "in_progress"

    def action_completed(self):
        for rec in self:
            rec.state = "completed"

    def action_close(self):
        for rec in self:
            rec.write({
                'state': 'closed'
            })

    def check_due_date(self):  
        tasks_ids = self.search([])
        for rec in tasks_ids:
            if rec.due_date and rec.due_date < fields.date.today() and rec.state != 'completed':
                rec.is_late = True
            else:
                rec.is_late = False

class TodoTimesheetLine(models.Model):
    _name = 'todo.timesheet.line'
    _description = 'To-do Time Sheet Line'

    task_id = fields.Many2one('todo.task')
    duration = fields.Float('Times In Hours', digits=(0, 2))
    date = fields.Date(default=fields.Date.today())
    description = fields.Text()