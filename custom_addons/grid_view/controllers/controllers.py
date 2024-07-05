# -*- coding: utf-8 -*-
# from odoo import http


# class GridView(http.Controller):
#     @http.route('/grid_view/grid_view', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/grid_view/grid_view/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('grid_view.listing', {
#             'root': '/grid_view/grid_view',
#             'objects': http.request.env['grid_view.grid_view'].search([]),
#         })

#     @http.route('/grid_view/grid_view/objects/<model("grid_view.grid_view"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('grid_view.object', {
#             'object': obj
#         })

