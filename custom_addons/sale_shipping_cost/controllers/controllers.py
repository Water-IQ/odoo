# -*- coding: utf-8 -*-
# from odoo import http


# class SaleShippingCost(http.Controller):
#     @http.route('/sale_shipping_cost/sale_shipping_cost', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_shipping_cost/sale_shipping_cost/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_shipping_cost.listing', {
#             'root': '/sale_shipping_cost/sale_shipping_cost',
#             'objects': http.request.env['sale_shipping_cost.sale_shipping_cost'].search([]),
#         })

#     @http.route('/sale_shipping_cost/sale_shipping_cost/objects/<model("sale_shipping_cost.sale_shipping_cost"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_shipping_cost.object', {
#             'object': obj
#         })

