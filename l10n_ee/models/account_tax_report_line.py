# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class AccountTaxReportLine(models.Model):
    _inherit = 'account.tax.report.line'

    emta_summary_name = fields.Char(string="EMTA Kokkuvõtte XML Silt")
    emta_classifier_code = fields.Char(string="EMTA Klassifikaatori Kood")
    emta_sum_all_children = fields.Boolean(string="EMTA Summeeri Kõik Alamad (nt rida 5)", default=False)
    emta_infb = fields.Boolean(string="EMTA INF B Kanded", default=False)

    emta_infa_code01 = fields.Boolean(string="EMTA INF A Erisuse Kood 01", default=False)
    emta_infb_code11 = fields.Boolean(string="EMTA INF B Erisuse Kood 11", default=False)
    #emta_infa_code03_check = fields.Boolean(string="EMTA INF A Erisuse Kood 03 käsitlus", default=False)

    emta_include_vat_cars = fields.Boolean(string="EMTA Kokkuvõte - VAT Cars", default=False)
    emta_include_vat_cars_partial = fields.Boolean(string="EMTA Kokkuvõte - VAT Cars Partial", default=False)
