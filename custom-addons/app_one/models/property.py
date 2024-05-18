from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Property(models.Model):
    _name = "property"
    _description ="Property"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    ref = fields.Char(default = 'New', readonly = True)
    name = fields.Char(required=True)  # Ensure required field
    description = fields.Text()
    postcode = fields.Char(tracking=1) 

    date_availability = fields.Date(tracking=1)
    expected_selling_date = fields.Date()
    is_late = fields.Boolean()  #compute="_compute_is_late"

    location = fields.Char(string="Location" , groups="app_one.property_manager_group")
    active = fields.Boolean(string="Active", default=True)

    expected_price = fields.Float()  # Allow null value for expected_price
    selling_price = fields.Float()  # Allow null value for selling_price
    difference = fields.Float(compute="_compute_difference")

    owner_id = fields.Many2one("owner")
    owner_phone = fields.Char(string="Owner's Phone", related='owner_id.phone', readonly=False)
    owner_address = fields.Char(string="Owner's Address", related='owner_id.address', readonly=False)

    create_time = fields.Datetime(string="Create Time", default=fields.Datetime.now)
    next_time = fields.Datetime(compute="_compute_next_time")

    tag_ids = fields.Many2many("tag")

    living_area = fields.Integer()
    bedrooms = fields.Integer()
    bathrooms = fields.Integer()
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

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("pending", "Pending"),
            ("sold", "Sold"),
            ("closed", "Closed"),
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

    bedroom_line_ids = fields.One2many("property.bedroom.line", "bed_property_id")
    bathroom_line_ids = fields.One2many("property.bathroom.line", "bath_property_id")

    @api.depends("create_time")
    def _compute_next_time(self):
        for rec in self:
            if rec.create_time:
                rec.next_time = rec.create_time + timedelta(hours=6)
            else:
                rec.next_time = False

    @api.depends("expected_price", "selling_price")
    def _compute_difference(self):
        for rec in self:
            rec.difference = rec.expected_price - rec.selling_price

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
            rec.create_history_record(rec.state, "draft")
            rec.state = "draft"

    def action_pending(self):
        for rec in self:
            rec.create_history_record(rec.state, "pending")
            rec.state = "pending"

    def action_sold(self):
        for rec in self:
            rec.create_history_record(rec.state, "sold")
            rec.state = "sold"

    def action_close(self):
        for rec in self:
            rec.create_history_record(rec.state, "closed")
            rec.state = "closed"

    def check_expected_selling_date(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.Date.today():
                rec.is_late = True

# 
    def action(self):
        print(self.env['property'].search(['|', ('name', 'ilike', 'Property'), ('garage', '!=', True)]))

    @api.model
    def create(self, vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env["ir.sequence"].next_by_code("property_seq")
        return res

    def create_history_record(self, old_state, new_state, reason=""):
        for rec in self:
            rec.env['property.history'].create({
                'user_id': self.env.uid,
                'property_id': rec.id,
                'old_state': old_state,
                'new_state': new_state,
                'reason': reason or "",
                'bedroom_history_line_ids': [(0, 0, {'description': line.description, 'area': line.area}) for line in rec.bedroom_line_ids],
                'bathroom_history_line_ids': [(0, 0, {'description': line.description, 'area': line.area}) for line in rec.bathroom_line_ids],
            })

    def action_open_change_state_wizard(self):
        action = self.env["ir.actions.actions"]._for_xml_id("app_one.action_change_state_wizard")
        action['context'] = {'default_property_id': self.id}
        return action

class PropertyBedroomLine(models.Model):
    _name = "property.bedroom.line"
    _description = "Property Bedroom Line"
    
    bed_property_id = fields.Many2one("property")
    area = fields.Float()
    description = fields.Char()
    
class PropertyBathroomLine(models.Model):
    _name = "property.bathroom.line"
    _description = "Property Bathroom Line"
    
    bath_property_id = fields.Many2one("property")
    area = fields.Float()
    description = fields.Char()

