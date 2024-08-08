# -*- coding: utf-8 -*-
# from odoo import http


# class EmailButton(http.Controller):
#     @http.route('/email_button/email_button', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/email_button/email_button/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('email_button.listing', {
#             'root': '/email_button/email_button',
#             'objects': http.request.env['email_button.email_button'].search([]),
#         })

#     @http.route('/email_button/email_button/objects/<model("email_button.email_button"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('email_button.object', {
#             'object': obj
#         })

