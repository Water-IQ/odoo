# -*- coding: utf-8 -*-
# from odoo import http


# class BarcodeSequence(http.Controller):
#     @http.route('/barcode_sequence/barcode_sequence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barcode_sequence/barcode_sequence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('barcode_sequence.listing', {
#             'root': '/barcode_sequence/barcode_sequence',
#             'objects': http.request.env['barcode_sequence.barcode_sequence'].search([]),
#         })

#     @http.route('/barcode_sequence/barcode_sequence/objects/<model("barcode_sequence.barcode_sequence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barcode_sequence.object', {
#             'object': obj
#         })

