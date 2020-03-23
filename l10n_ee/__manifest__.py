# -*- coding: utf-8 -*-
# Part of EST-POS OÜ Common Modules and Localization. See LICENSE file for full copyright and licensing details.

{
    'name': 'Estonian Accounting',
    'version': '1.0',
    'author': u'EST-POS OÜ',
    'license': 'OPL-1',
    'website': 'https://estpos.ee',
    'category': 'Localization',
    'depends': [
        'account',
        'account_accountant',
    ],
    'data': [
        'views/account_financial.xml', 
        'data/account_chart_template.xml',
        'data/account_financial_html_report.xml',
        'data/account_tax_group.xml',
        'data/account_account_tag.xml',
        'data/account_account_template.xml',
        'data/account_tax_report_data.xml',
        'data/account_tax_data.xml',

        'data/res_country_state.xml',
        'data/fiscal_position_template.xml',

        'security/ir.model.access.csv',
        
        'views/vat_cars.xml',
        'views/res_partner.xml',
        'views/account_move_view.xml',
    ],
    'description': u'''
This module provides the standard Accounting Chart for Estonia
==============================================================
Please keep in mind that you should review and adapt it with your Accountant, 
before using it in a live Environment.
''',
}
