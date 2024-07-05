# -*- coding: utf-8 -*-

from odoo import models, fields, api


class View(models.Model):
    """Extends the base ir.ui.view model to include a new type of view."""

    _inherit = "ir.ui.view"
    type = fields.Selection(selection_add=[("grid", "Grid")])


class IrActionsActWindowView(models.Model):
    """Extends the base ir.actions.act_window.view model to include a new view model."""

    _inherit = "ir.actions.act_window.view"
    view_mode = fields.Selection(
        selection_add=[("grid", "Grid")], ondelete={"grid": "cascade"}
    )
