from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = "property"

    name = fields.Char(required=True)  # Ensure required field
    description = fields.Text(required=True)  # Ensure required field
    postcode = fields.Char(required=True)  # Ensure required field
    date_availability = fields.Date(required=True)  # Ensure required field
    location = fields.Char(string="Location")

    expected_price = fields.Float()  # Allow null value for expected_price
    selling_price = fields.Float()  # Allow null value for selling_price
    differance = fields.Float(compute="_compute_differance")
    
    owner_id = fields.Many2one("owner")
    owner_phone = fields.Char(string="Owner's Phone", related='owner_id.phone', readonly=False)
    owner_address = fields.Char(string="Owner's Address", related='owner_id.address', readonly=False)

    living_area = fields.Integer()
    bedrooms = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
    property_value = fields.Selection(
        string="Property Value",
        selection=[
            ("low", "Low Budget Property"),
            ("med", "Med Budget Property"),
            ("high", "High Budget Property"),
        ],
    )

    property_width = fields.Selection(
        string="Property Width",
        selection=[
            ("small", "Small Apartment"),
            ("med", "Medium Apartment"),
            ("wide", "Wide Apartment"),
        ],
    )


    
    tag_ids = fields.Many2many("tag")

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("sold", "Sold"),
        ],
        default="draft",
    )

    _sql_constraints = [
        ("unique_name", "unique(name)", "This Name is Exist!"),
        (
            "unique_description",
            "unique(description)",
            "This Description is Already Exist!",
        ),
    ]

    @api.depends("expected_price", "selling_price")
    def _compute_differance(self):
        for rec in self:
            rec.differance = rec.expected_price - rec.selling_price

    @api.onchange("bedrooms")
    def _onchange_bedrooms(self):
        for rec in self:
            if rec.bedrooms > 5:
                print("more than 5")
            else:
                print("less than or equal to 5")

    @api.onchange("expected_price")
    def _onchange_expected_price(self):
        for rec in self:
            if rec.expected_price < 100000:
                rec.property_value = "low"
            elif 100000 < rec.expected_price < 500000:
                rec.property_value = "med"
            else:
                rec.property_value = "high"

    @api.onchange("living_area")
    def _onchange_living_area(self):
        for rec in self:
            if rec.living_area < 100:
                rec.property_width = "small"
            elif 100 < rec.living_area < 200:
                rec.property_width = "med"
            else:
                rec.property_width = "wide"

    @api.constrains("expected_price", "selling_price")
    def _check_price_validity(self):
        for rec in self:
            if rec.expected_price is not None and rec.expected_price <= 0:
                raise ValidationError("Expected Price must be a positive number.")
            if rec.selling_price is not None and rec.selling_price <= 0:
                raise ValidationError(
                    "Selling Price must be a positive number or zero."
                )

            # Optional validation: Check if selling price is lower than expected price (if both are provided)
            if (
                rec.expected_price is not None
                and rec.selling_price is not None
                and rec.selling_price > rec.expected_price
            ):
                raise ValidationError(
                    "Selling Price cannot be higher than Expected Price."
                )

    def action_garden(self):
        for rec in self:
            print("inside the garden action")
            rec.garden = "1"

    def action_money(self):
        for rec in self:
            print("inside the money action")
            rec.expected_price = +1000

    def action_draft(self):
        for rec in self:
            print("inside draft action")
            rec.state = "draft"

    def action_pending(self):
        for rec in self:
            print("inside pending action")
            rec.state = "pending"

    def action_sold(self):
        for rec in self:
            print("inside the sold action")
            rec.state = "sold"

    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super(Property, self).create(vals_list)
    #     print("Hello from create method")
    #     return res
    #
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None, access_rights_uid=None):
    #     res = super(Property, self)._search(
    #         domain, offset=0, limit=None, order=None, access_rights_uid=None
    #     )
    #     print("Hello from search method")
    #     return res
    #
    # def write(self, vals_list):
    #     res = super(Property, self).write(vals_list)
    #     print("Hello from write method")
    #     return res
    #
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("Hello from unlink method")
    #     return res
