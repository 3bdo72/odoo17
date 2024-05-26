from odoo import http

class TestApi(http.Controller):
    @http.route('/test_api', type='http', auth="none", methods=['GET'], csrf=False)
    def index(self, **kw):
        return 'Hello, World!'