# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sample_results(models.Model):
    _name = 'sample_results'

    contact = fields.Char(string="Contact Info", max_length=50, stored=True, null=True, default="N/A")
    dealer = fields.Char(string="Dealer", max_length=50, stored=True, null=True, default="N/A")
    sampling_date = fields.Date(string="Sampling Date",stored=True, null=True, default=None)
    sample_location = fields.Char(string="Sample Location", max_length=50, stored=True, null=True, default=None)
    dom_algae_diatoms = fields.Char(string="Dominant Algae/Diatoms", max_length=50, stored=True, null=True, default=None)
    sec_algae_diatoms = fields.Char(string="Secondary Algae/Diatoms", max_length=50, stored=True, null=True, default=None)
    state_city = fields.Char(string="State/City", max_length=50, stored=True, null=True, default=None)
    report_send_date = fields.Date(string="Report Sent", stored=True, null=True, default=None)
    extra_info = fields.Text(string="Additional Info", stored=True, null=True, default=None)

    

