from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'ref'

    ref = fields.Char(string="Reference", default="New", readonly=True)
    active = fields.Boolean(string="Active", default=True)
    #Core Appointment Fields:
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], related='patient_id.gender', readonly=True)
    age = fields.Integer(readonly=True, compute='_compute_age' , store=True)
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
    appointment_date = fields.Datetime(default=fields.Datetime.now)
    booking_date = fields.Date(default=fields.Date.context_today)
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

    # Notebook
    prescription_ids = fields.One2many('medical.prescription.line', 'medicine_appointment_id', string="Medicines")
    allergy_ids = fields.One2many('allergy.line', 'allergy_appointment_id', string="Allergies")

    # Status
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_consolation', 'In Consolation'),
        ('done', 'Done'),
        ('canceled', 'Canceled'),
    ])

    @api.model
    def create(self, vals):
        if vals.get('ref', 'New') == 'New':
            vals['ref'] = self.env['ir.sequence'].next_by_code('appointment_ref') or 'New'
        return super(HospitalAppointment, self).create(vals)

    @api.depends('patient_id')
    def _compute_age(self):
        for rec in self:
            rec.age = rec.patient_id.age

    def action_draft(self):
        for rec in self:
            rec.status = 'draft'

    def action_in_consolation(self):
        for rec in self:
            rec.status = 'in_consolation'

    def action_done(self):
        for rec in self:
            rec.status = 'done'

    def action_canceled(self):
        for rec in self:
            rec.status = 'canceled'

class MedicalPrescriptionLine(models.Model):
    _name = 'medical.prescription.line'
    _description = 'Medical Prescriptions'

    counter = fields.Integer(string="Counter", readonly=True, compute='_compute_sequence')
    medicine = fields.Char(string="Medicine", required=True)
    medicine_appointment_id = fields.Many2one('hospital.appointment', string="Patient", domain="[('active', '=', True)]")
    doctor_id = fields.Many2one('res.partner', string="Doctor", domain="[('is_doctor', '=', True)]")

    dosage = fields.Float(string="Dosage", required=True)
    dosage_unit = fields.Char(string="Dosage Unit", required=True)
    frequency = fields.Selection([
        ('daily', 'Daily'),
        ('twice_daily', 'Twice Daily'),
        ('as_needed', 'As Needed'),
    ], string="Frequency", required=True)
    duration = fields.Integer(string="Duration (Days)")
    instructions = fields.Text(string="Instructions")

    # Optional Fields (consider based on your needs)
    route = fields.Selection([
        ('oral', 'Oral'),
        ('topical', 'Topical'),
        ('intravenous', 'Intravenous'),
    ], string="Route")
    refills = fields.Integer(string="Refills")
    dispense_unit = fields.Char(string="Dispense Unit")
    special_instructions = fields.Text(string="Special Instructions")
    note = fields.Text(string="Note")

    @api.depends('medicine_appointment_id')
    def _compute_sequence(self):
        for rec in self:
            counter = 1
            for line in rec.medicine_appointment_id.prescription_ids:
                line.counter = counter
                counter += 1

class AllergyLine(models.Model):
    _name = 'allergy.line'
    _description = 'Allergies'

    counter = fields.Integer(string="Counter", readonly=True, compute='_compute_sequence')
    allergy_name = fields.Char(string="Allergy", required=True)
    allergy_appointment_id = fields.Many2one('hospital.appointment', string="Patient")

    reaction = fields.Char(string="Reaction")
    severity = fields.Selection([
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ], string="Severity")
    onset = fields.Char(string="Onset")

    # Optional Fields (consider based on your needs)
    trigger = fields.Char(string="Trigger")
    diagnosed_date = fields.Date(string="Diagnosed Date")
    note = fields.Text(string="Note")
    management = fields.Text(string="Management")
    reference = fields.Char(string="Reference")

    # Compute the sequence for allergy lines based on the related appointment
    @api.depends('allergy_appointment_id')
    def _compute_sequence(self):
        for rec in self:
            counter = 1
            for line in rec.allergy_appointment_id.allergy_ids:
                line.counter = counter
                counter += 1