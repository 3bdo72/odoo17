# from typing import re

from odoo import models, fields

# from odoo.exceptions import ValidationError


class Owner(models.Model):
    _name = "owner"
    _description = "Owner Details for the Property"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    address = fields.Char(string="Address")

    property_ids = fields.One2many("property", "owner_id")
    
    _sql_constraints = [
        ("unique_name", "unique(name)", "This Name is Exist!"),
        ('unique_phone_num', 'unique(phone)', 'This Phone Already Exist!'),
        ('unique_address', 'unique(address)', 'This Address Already Exist!'),
    ]
    

    # @api.constrains("phone")
    # def _check_phone_format(self):
    #     for record in self:
    #         phone_format = r"0\d{2}-\d{3}-\d{4}"  # Egyptian phone number format
    #         if not re.match(phone_format, record.phone):
    #             raise ValidationError(
    #                 _(
    #                     "Invalid phone number format. Please use a valid Egyptian phone number (e.g., 010-123-4567)."
    #                 )
    #             )
