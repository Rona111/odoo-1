# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2015 Elico Corp (<http://www.elico-corp.com>)
#    Authors: Luke Zheng
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
    'name': 'Portal Usability',
    'version': '0.1',
    'category': '',
    'depends': [
        'sale',
        'stock',
        'portal_stock',
        'portal_sale',
        'web'
    ],
    'author': 'Elico Corp',
    'license': 'AGPL-3',
    'website': 'https://www.elico-corp.com',
    'description': """

what this module has done:

    add a specific form view for stock picking for portal user.
    add a new form view & menu for res_user model.
    remove the items on the topright: Reference & My Odoo account etc.
    allow user to change their delivery address and personal information eg, phone number.

    """,
    'images': [],
    'demo': [],
    'data': [
        'views/portal_view_associator.xml',
        'views/wizard_change_password.xml',
        'security/ir.model.access.csv',
        'security/portal_security.xml'
    ],
    'qweb': ['static/src/xml/portal_base.xml'],
    'test': [],
    'installable': True,
    'application': False

}
