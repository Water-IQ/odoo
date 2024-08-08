# -*- coding: utf-8 -*-
# from odoo import http


# class SampleResults(http.Controller):
#     @http.route('/sample_results/sample_results', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sample_results/sample_results/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sample_results.listing', {
#             'root': '/sample_results/sample_results',
#             'objects': http.request.env['sample_results.sample_results'].search([]),
#         })

#     @http.route('/sample_results/sample_results/objects/<model("sample_results.sample_results"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sample_results.object', {
#             'object': obj
#         })

