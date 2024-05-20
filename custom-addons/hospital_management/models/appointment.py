from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(string="Reference", default="New", readonly=True)
    #Core Appointment Fields:
    name = fields.Char()
    patient_id = fields.Many2one('hospital.patient')
    doctor_id = fields.Many2one('hospital.doctor')
    appointment_type = fields.Selection([
        ('general', 'General Consultation'),
        ('cardiology', 'Cardiology'),
        ('orthopedics', 'Orthopedics'),
        ('neurology', 'Neurology'),
        ('oncology', 'Oncology'),
        ('emergency', 'Emergency'),
        ('other', 'Other'),
        ])
    appointment_date = fields.Datetime()
    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('confirmed', 'Confirmed'),
        ('arrived', 'Arrived'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rescheduled', 'Rescheduled'),
        ('canceled', 'Canceled'),
        ])
    duration = fields.Integer()

    #Additional Fields for Enhanced Functionality:
    urgency_level = fields.Selection([
        ('non', 'Non-Urgent'),
        ('urg', 'Urgent'),
        ('crit', 'Critical'),
    ])
    notes = fields.Text()
    internal_notes = fields.Text()
    attachments = fields.Binary()
    pre_consolation_questions = fields.Text()
    follow_up_appointments = fields.Boolean()
    payment_status = fields.Selection([
        ('not_billed', 'Not Billed'),
        ('billed', 'Billed'),
        ('paid', 'Paid'),
        ('partial', 'Partially Paid'),
    ])
    insurance = fields.Boolean()

    @api.model
    def create(self, vals):
        if vals.get('ref', 'New') == 'New':
            vals['ref'] = self.env['ir.sequence'].next_by_code('appointment_ref') or 'New'
        return super(HospitalAppointment, self).create(vals)