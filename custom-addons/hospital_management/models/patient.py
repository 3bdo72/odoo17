from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    ref = fields.Char(string="Reference", default = "New", readonly=True)
    name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male')
    # doctor = fields.Many2one('hospital.doctor', ondelete='set null', index=True, null=True)

    @api.model
    def create(self, vals):
        res = super(HospitalPatient, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env["ir.sequence"].next_by_code("patient_ref")
        return res