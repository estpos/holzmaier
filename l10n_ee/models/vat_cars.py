from odoo import models, fields, _


class VATCars(models.Model):
    _name = 'vat.cars'
    _description = 'l10n ee VAT Cars'

    start_date = fields.Date(
        string=_('Start date'),
        required=True,
    )
    end_date = fields.Date(
        string=_('End date'),
        required=True,
    )
    type = fields.Selection(
        [
            ('business', 'Business Car'),
            ('partially_business', 'Partially Business Car'),
        ],
        string=_('Type'),
    )
    plate_number = fields.Char(
        string=_('Plate number'),
        required=True,
    )
    description = fields.Char(
        string=_('Description (Optional)'),
    )
