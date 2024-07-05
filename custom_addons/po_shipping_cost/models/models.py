# -*- coding: utf-8 -*-

from odoo import models, fields, api

class po_form_line(models.Model):
    _inherit = "purchase.order.line"
    po_tax = fields.Float(string="Tax", stored=True)


class POShippingCost(models.Model):
    _inherit = "purchase.order"

    po_shipping_cost = fields.Monetary(
        string="Shipping Cost", currency_field="currency_id"
    )

    @api.depends("order_line.price_total", "po_shipping_cost", "order_line.po_tax")
    def _amount_all(self):
        super(POShippingCost, self)._amount_all()
        for order in self:
            amount_untaxed = po_tax_total = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                po_tax_total += line.po_tax
            order.update(
                {
                    "amount_untaxed": amount_untaxed,
                    "amount_tax": po_tax_total,
                    "amount_total": amount_untaxed
                    + po_tax_total
                    + order.po_shipping_cost,
                }
            )

    def _prepare_invoice(self):
        invoice_vals = super(POShippingCost, self)._prepare_invoice()
        shipping_line = {
            "name": "Shipping Cost",
            "quantity": 1,
            "price_unit": self.po_shipping_cost,
        }
        tax_line = {
            "name": "Tax Amount",
            "quantity": 1,
            "price_unit": sum(line.po_tax for line in self.order_line),
        }
        invoice_vals["invoice_line_ids"].append((0, 0, shipping_line))
        invoice_vals["invoice_line_ids"].append((0, 0, tax_line))
        return invoice_vals

    """
        In Odoo, the notation (0, 0, {...}) is used within the context of a one2many or many2many field to indicate that a new record should be created with the specified values.
        0: Indicates that this is an operation type for creating a new record.
        0: The second 0 is a placeholder for the ID of the record being created, which is 0 because the record does not yet exist.
    """

    @api.onchange('po_shipping_cost', 'order_line.po_tax')
    def _onchange_po_shipping_cost(self):
        """
        update price total to include shipping cost & tax cost
        """
        self._amount_all()
