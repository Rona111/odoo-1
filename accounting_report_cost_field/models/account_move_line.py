# -*- coding: utf-8 -*-
# © <2015> <Siyuan Gu>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    cost = fields.Float(readonly=True, related='product_id.standard_price')
