# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010-2015 Elico Corp (<http://www.elico-corp.com>)
#    Authors: Siyuan Gu
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
from openerp import models, fields, api, exceptions, _


class StockInventory(models.Model):
    _inherit = "stock.inventory"

    _order = "product_id"

    @api.model
    def _get_available_filters(self):
        res = super(StockInventory, self)._get_available_filters()
        res.append(('file', _('By File')))
        return res

    @api.depends('import_lines')
    def _file_lines_processed(self):
        processed = True
        if self.import_lines:
            processed = any((not line.fail or
                             (line.fail and
                              line.fail_reason != _('No processed')))
                            for line in self.import_lines)
        self.processed = processed

    imported = fields.Boolean('Imported')
    import_lines = fields.One2many('stock.inventory.import.line',
                                   'inventory_id', string='Imported Lines')
    filter = fields.Selection(_get_available_filters,
                              string='Selection Filter',
                              required=True)
    processed = fields.Boolean(string='Has been processed at least once?',
                               compute='_file_lines_processed')

    @api.one
    def process_import_lines(self):
        """Process Inventory Load lines."""
        if not self.import_lines:
            raise exceptions.Warning(_("There must be one line at least to "
                                       "process"))
        inventory_line_obj = self.env['stock.inventory.line']
        stk_lot_obj = self.env['stock.production.lot']
        product_obj = self.env['product.product']
        for line in self.import_lines:
            if not line.product:
                prod_lst = product_obj.search([('ean13', '=',
                                                line.code)])
                if prod_lst:
                    product = prod_lst[0]
                else:
                    line.fail_reason = _('No Ean13 Barcode found')
                continue
            else:
                product = line.product
            lot_id = None
            if line.lot:
                lot_lst = stk_lot_obj.search([('name', '=', line.lot)])
                if lot_lst:
                    lot_id = lot_lst[0].id
                else:
                    lot = stk_lot_obj.create({'name': line.lot,
                                              'product_id': product.id})
                    lot_id = lot.id

            if line.fail:
                inventory_line_obj.create({'product_id': product.id,
                                           'product_uom_id': product.uom_id.id,
                                           'product_qty': line.quantity,
                                           'inventory_id': self.id,
                                           'location_id': line.location_id.id,
                                           'prod_lot_id': lot_id})
                line.write({'fail': False, 'fail_reason': _('Processed')})
            else:
                for record in self.line_ids:
                    if record.product_id.id == product.id:
                        record['product_qty'] = line.quantity

        return True

    @api.multi
    def action_done(self):
        for inventory in self:
            if not inventory.processed:
                raise exceptions.Warning(
                    _("Loaded lines must be processed at least one time for "
                      "inventory : %s") % (inventory.name))
            super(StockInventory, inventory).action_done()
