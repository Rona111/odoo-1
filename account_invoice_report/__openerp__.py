# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright Liping Wang
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Invoice Report',
    'version': '8.0.1.0.0',
    'category': '',
    'depends': ['stock', 'sale'],
    'author': 'Elico Corp',
    'license': 'AGPL-3',
    'website': 'https://www.elico-corp.com',
    'data': [
        'invoice_report.xml',
        'views/report_saleorder_extend.xml',
        'views/report_invoice_extend.xml',
        'views/report_stockpicking_extend.xml',
        'views/report_stockpicking_extend_full.xml',
        'views/invoice_report.xml',
        'views/report_draft_order_invoice.xml',
        'company_view.xml'
    ],
    'installable': True,
    'application': False,
}
