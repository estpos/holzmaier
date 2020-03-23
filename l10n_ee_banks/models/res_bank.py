from odoo import api, models, fields, _
from .iban import *
import re

STATES = [
    ('EE', 'Estonia'), ('AD', 'Andorra'), ('AL', 'Albania'), ('AT', 'Austria'),
    ('BA', 'Bosnia and Herzegovina'), ('BE', 'Belgium'), ('BG', 'Bulgaria'),
    ('CH', 'Switzerland'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'),
    ('DE', 'Germany'), ('DK', 'Denmark'), ('ES', 'Spain'), ('FI', 'Finland'),
    ('FO', 'Faroe Islands'), ('FR', 'France'), ('GB', 'United Kingdom'),
    ('GE', 'Georgia'), ('GI', 'Gibraltar'), ('GL', 'Greenland'),
    ('GR', 'Greece'), ('HR', 'Croatia'), ('HU', 'Hungary'), ('IE', 'Ireland'),
    ('IL', 'Israel'), ('IS', 'Iceland'), ('IT', 'Italy'), ('KW', 'Kuwait'),
    ('KZ', 'Kazakhstan'), ('LB', 'Lebanon'), ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('LV', 'Latvia'),
    ('MC', 'Monaco'), ('ME', 'Montenegro'),
    ('MK', 'Macedonia, Former Yugoslav Republic of'), ('MR', 'Mauritania'),
    ('MT', 'Malta'), ('MU', 'Mauritius'), ('NL', 'Netherlands'),
    ('NO', 'Norway'), ('PL', 'Poland'), ('PT', 'Portugal'), ('RO', 'Romania'),
    ('RS', 'Serbia'), ('SA', 'Saudi Arabia'), ('SE', 'Sweden'),
    ('SI', 'Slovenia'), ('SK', 'Slovak Republic'), ('SM', 'San Marino'),
    ('TN', 'Tunisia'), ('TR', 'Turkey'),
]


class ResBank(models.Model):
    _inherit = 'res.bank'

    iban_id_code = fields.Integer(
        string=_('IBAN Code'),
    )


class ResBankAccount(models.Model):
    _inherit = 'res.partner.bank'

    country = fields.Selection(
        string=_('Country'),
        selection=STATES,
    )

    @api.onchange('acc_number')
    def onchange_acc_number(self):
        if self.acc_number:
            if re.search('[a-zA-Z]', self.acc_number):
                self.calc_bank_name()
            else:
                self.calc_iban()

    @api.model
    def calc_bank_name(self):
        if self.acc_number:
            self.state = "iban"
            acc_number_len = len(self.acc_number)

            if acc_number_len == 20:
                iban_id = int(self.acc_number[4:6])
            elif acc_number_len == 24:
                iban_id = int(self.acc_number[5:7])
            else:
                return

            dom = [('iban_id_code', '=', iban_id)]
            bank_id = self.env['res.bank'].search(dom)
            self.bank_id = bank_id

    @api.model
    def calc_iban(self):
        '''For Estonian accounts'''
        self.country = "EE"
        self.acc_number = create_iban(
            str(self.country),
            str(self.acc_number[0:2]),
            str(self.acc_number)
        )
        self.calc_bank_name()
