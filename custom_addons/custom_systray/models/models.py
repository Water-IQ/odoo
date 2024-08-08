# -*- coding: utf-8 -*-
from odoo import models, fields, api


class CustomSystray(models.Model):
    _name = 'custom.systray'

    @api.model
    def get_ticker_data(self):

        self.env.cr.execute(
            """
            SELECT product_id, SUM(product_uom_qty) as total_qty
            FROM sale_order_line
            WHERE product_id IS NOT NULL AND product_id IN (
                SELECT pp.id FROM product_product pp
                JOIN product_template pt ON pp.product_tmpl_id = pt.id
                WHERE pt.sale_ok = TRUE AND pt.type != 'service'
            )
            GROUP BY product_id
            ORDER BY total_qty DESC
            LIMIT 1
        """
        )
        top_product_data = self.env.cr.dictfetchone()
        top_product = self.env['product.product'].browse(top_product_data['product_id']) if top_product_data else None

        confirmed_orders = self.env["sale.order"].search(
            [("state", "in", ["sale", "done"])]
        )
        total_revenue = sum(confirmed_orders.mapped("amount_total"))

        total_orders = confirmed_orders.search_count([])

        return f"Best Selling: {top_product.name if top_product else 'N/A'}, Revenue: {total_revenue}, Orders: {total_orders}"
