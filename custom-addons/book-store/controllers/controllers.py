# -*- coding: utf-8 -*-
# from odoo import http


# class Book-store(http.Controller):
#     @http.route('/book-store/book-store', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/book-store/book-store/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('book-store.listing', {
#             'root': '/book-store/book-store',
#             'objects': http.request.env['book-store.book-store'].search([]),
#         })

#     @http.route('/book-store/book-store/objects/<model("book-store.book-store"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('book-store.object', {
#             'object': obj
#         })

