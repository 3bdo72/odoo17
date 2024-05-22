from odoo.tests.common import TransactionCase
from odoo import fields

class TestProperty(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestProperty, self).setUp(*args, **kwargs)
        
        self.property_01_record = self.env['app_one.property'].create({
            'ref': 'PRT1000',
            'name': 'Property 1000',
            'description': 'Property Description 1000',
            'postcode': '1010',
            'date_availability': fields.Date.today(),
            'location': 'Location 1000',
            'expected_price': 9000,
            'selling_price': 8000,
            'bedrooms': 3,
        })

    def test_property_01_values(self):
        property_id = self.property_01_record
        
        self.assertRecordValues(property_id, [
            ('ref', 'PRT1000'),
            ('name', 'Property 1000'),
            ('description', 'Property Description 1000'),
            ('postcode', '1010'),
            ('date_availability', fields.Date.today()),
            ('location', 'Location 1000'),
            ('expected_price', 9000),
            ('selling_price', 8000),
            ('bedrooms', 3),
        ])