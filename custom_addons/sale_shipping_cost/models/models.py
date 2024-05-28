# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleShippingCost(models.Model):
    _inherit = "sale.order"

    sale_shipping_cost = fields.Monetary(
        string="Shipping Cost", currency_field="currency_id"
    )

    @api.depends("order_line.price_total", "sale_shipping_cost")
    def _amount_all(self):
        super(SaleShippingCost, self)._amount_all()
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update(
                {
                    "amount_untaxed": amount_untaxed,
                    "amount_tax": amount_tax,
                    "amount_total": amount_untaxed
                    + amount_tax
                    + order.sale_shipping_cost,
                }
            )

    def _prepare_invoice(self):
        invoice_vals = super(SaleShippingCost, self)._prepare_invoice()
        shipping_line = {
            "name": "Shipping Cost",
            "quantity": 1,
            "price_unit": self.sale_shipping_cost,
        }
        invoice_vals["invoice_line_ids"].append((0, 0, shipping_line))
        return invoice_vals

    """
        In Odoo, the notation (0, 0, {...}) is used within the context of a one2many or many2many field to indicate that a new record should be created with the specified values.
        0: Indicates that this is an operation type for creating a new record.
        0: The second 0 is a placeholder for the ID of the record being created, which is 0 because the record does not yet exist.
    """

    @api.onchange(sale_shipping_cost)
    def _onchange_sale_shipping_cost(self):
        """
        update price total to include shipping cost
        """
        self._amount_all()
