# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'

    code = fields.Char(
        string=_('Code'),
        required=True,
    )
