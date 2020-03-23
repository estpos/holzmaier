# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Partner(models.Model):
    _inherit = 'res.partner'

    reg_number = fields.Char(
        string=_('Registration Number'),
    )
    is_vd = fields.Boolean(
        string=_('VAT Declaration Partner'),
    )
