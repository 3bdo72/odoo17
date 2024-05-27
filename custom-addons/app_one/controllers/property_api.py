import json
from odoo import http
from odoo.http import request

    # APIs in Odoo (CRUD) 1. Create Operation (POST)
    # We can use POST method to create new records.
    # We Have 2 types of POST methods:
    # 1. Create (POST)
    # 2. Update (PUT)
class PropertyApi(http.Controller):
    @http.route('/v1/property', type='http', auth="none", methods=['POST'], csrf=False)
    def post_property(self):
        args = request.httprequest.data.decode()
        vals = json.loads(args)
        res = request.env['property'].sudo().create(vals)
        if res:
            return request.make_json_response({
                "message": "Property created successfully",
            }, status=200)