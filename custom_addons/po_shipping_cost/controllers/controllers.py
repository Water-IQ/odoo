# -*- coding: utf-8 -*-
# from odoo import http


# class PoShippingCost(http.Controller):
#     @http.route('/po_shipping_cost/po_shipping_cost', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/po_shipping_cost/po_shipping_cost/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('po_shipping_cost.listing', {
#             'root': '/po_shipping_cost/po_shipping_cost',
#             'objects': http.request.env['po_shipping_cost.po_shipping_cost'].search([]),
#         })

#     @http.route('/po_shipping_cost/po_shipping_cost/objects/<model("po_shipping_cost.po_shipping_cost"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('po_shipping_cost.object', {
#             'object': obj
#         })

