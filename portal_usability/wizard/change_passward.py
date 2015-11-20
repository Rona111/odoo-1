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
from openerp import models, fields, api, _
import openerp.exceptions
from openerp.exceptions import Warning


class WizardChangePassword(models.TransientModel):
    _name = 'wizard.change.password'

    old_passwd = fields.Char('old_passwd')
    new_passwd = fields.Char('new_passwd')
    confirmed_new_passwd = fields.Char('confirmed_new_passwd')

    @api.one
    def change_password(self):
        if self.new_passwd != self.confirmed_new_passwd:
            raise Warning(_("New passwords is not the same!"))
        try:
            self.env['res.users'].browse(self.env.uid).change_password(
                self.old_passwd, self.new_passwd)
        except openerp.exceptions.AccessDenied:
            raise Warning(_("Old passwords is not the correct!"))
