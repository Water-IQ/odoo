# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

class EmailButton(models.Model):
    # _inherit = 'studio_customization'

    # user_id = fields.Many2one('res.users', string='User')

    def action_update_status_and_notify(self):
        self.ensure_one()
        self.status = 'Shipped'

        # send email to the user that made request
        template = self.env.ref('email_button.email_template_request_notification')

        if template:
            template.send_mail(self.id, force_send=True)
        else:
            raise UserError("Email template not found!")
        
        
        return True

