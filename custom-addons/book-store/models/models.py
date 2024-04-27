# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookStore(models.Model):
    _name = "book.store"
    _description = "this is description"

    # SIMPLE FIELDS
    name = fields.Char(string="What's ur Name?")
    email = fields.Char(string="What's ur Email?")
    password = fields.Char(string="Password")
    age = fields.Integer(string="How old are u?")
    money = fields.Float(string="How much money do u have?")
    description = fields.Text(string="Tell me about ur self.")
    boolean = fields.Boolean(string="Do u love ur Parents?, if yes check this box.")
    gender = fields.Selection(
        string="Gender", selection=[("m", "Male"), ("f", "Female"), ("other", "Other")]
    )

    Toys = fields.Selection(
        string="Toy",
        selection=[
            ("car", "Car"),
            ("plane", "Plane"),
            ("doll", "Doll"),
            ("train", "Train"),
            ("shotgun", "Shotgun"),
        ],
    )
    HTML = fields.Html()
    Date = fields.Date(string="Date of Birth")
    DateTime = fields.Datetime()
    binary = fields.Binary()


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
