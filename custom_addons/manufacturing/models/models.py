# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BoMs(models.Model):
    _inherit = "mrp.bom"

    bom_cost = fields.Float(string="BoM Cost", compute="_compute_bom_cost", store=True)
    barcode = fields.Char(
        related="product_tmpl_id.barcode", string="Barcode", store=True
    )

    @api.depends("bom_line_ids.product_qty", "bom_line_ids.product_id.standard_price")
    def _compute_bom_cost(self):
        for bom in self:
            total_cost = 0.0
            for line in bom.bom_line_ids:
                total_cost += line.product_qty * line.product_id.standard_price
            bom.bom_cost = total_cost

class BoMLines(models.Model):
    _inherit = "mrp.bom.line"

    barcode = fields.Char(related="product_tmpl_id.barcode", string="Barcode", store=True)
