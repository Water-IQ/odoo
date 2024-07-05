# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_inventory(models.Model):
    _inherit = "product.template"

    mpn = fields.Char(string="MPN", max_length=20, stored=True)
    location = fields.Char(string="Location", max_length=20, stored=True)
    standard_price = fields.Float(string="Cost", stored=True)

