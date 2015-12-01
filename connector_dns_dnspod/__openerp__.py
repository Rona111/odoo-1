# -*- coding: utf-8 -*-
# © 2015 Elico corp (www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'DNSpod connector',
    'version': '8.0.1.0.1',
    'category': 'Connector',
    'depends': [
        'connector_dns',
    ],
    'author': 'Elico Corp',
    'license': 'AGPL-3',
    'website': 'https://www.elico-corp.com',
    'data': [
        'security/connector_group.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False
}
