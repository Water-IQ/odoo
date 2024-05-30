# -*- coding: utf-8 -*-

from odoo import models, fields, api


class barcode_sequence(models.Model):
    _inherit = "product.product"

    barcode = fields.Char(string="Barcode", store=True, default="/")

    # On create method
    @api.model
    def create(self, vals):
        if vals.get("barcode", "/") == "/":
            vals["barcode"] = (
                self.env["ir.sequence"].get("barcode.sequence.code") or "/"
            )
        return super(barcode_sequence, self).create(vals)
