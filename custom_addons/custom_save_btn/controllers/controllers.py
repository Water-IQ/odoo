# -*- coding: utf-8 -*-
# from odoo import http


# class CustomSaveBtn(http.Controller):
#     @http.route('/custom_save_btn/custom_save_btn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_save_btn/custom_save_btn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_save_btn.listing', {
#             'root': '/custom_save_btn/custom_save_btn',
#             'objects': http.request.env['custom_save_btn.custom_save_btn'].search([]),
#         })

#     @http.route('/custom_save_btn/custom_save_btn/objects/<model("custom_save_btn.custom_save_btn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_save_btn.object', {
#             'object': obj
#         })

