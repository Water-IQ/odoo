# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSystray(http.Controller):
#     @http.route('/custom_systray/custom_systray', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_systray/custom_systray/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_systray.listing', {
#             'root': '/custom_systray/custom_systray',
#             'objects': http.request.env['custom_systray.custom_systray'].search([]),
#         })

#     @http.route('/custom_systray/custom_systray/objects/<model("custom_systray.custom_systray"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_systray.object', {
#             'object': obj
#         })

