# -*- coding: utf-8 -*-
# © 2017 Elico Corp (www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class ProjectProjectCategory(models.Model):
    _inherit = 'project.project.category'

    br_required = fields.Boolean(
        'Business Requirement required',
        help='If marked as true the business requirement'
        ' link in the task linked to this project will be mandatory')
