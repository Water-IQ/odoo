# -*- coding: utf-8 -*-
# from odoo import http


# class WebEnterprise(http.Controller):
#     @http.route('/web_enterprise/web_enterprise', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/web_enterprise/web_enterprise/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('web_enterprise.listing', {
#             'root': '/web_enterprise/web_enterprise',
#             'objects': http.request.env['web_enterprise.web_enterprise'].search([]),
#         })

#     @http.route('/web_enterprise/web_enterprise/objects/<model("web_enterprise.web_enterprise"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('web_enterprise.object', {
#             'object': obj
#         })

