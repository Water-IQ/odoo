# -*- coding: utf-8 -*-
# from odoo import http


# class Manufacturing(http.Controller):
#     @http.route('/manufacturing/manufacturing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manufacturing/manufacturing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manufacturing.listing', {
#             'root': '/manufacturing/manufacturing',
#             'objects': http.request.env['manufacturing.manufacturing'].search([]),
#         })

#     @http.route('/manufacturing/manufacturing/objects/<model("manufacturing.manufacturing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manufacturing.object', {
#             'object': obj
#         })

