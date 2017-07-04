# -*- coding: utf-8 -*-
# © 2016 Elico Corp (www.elico-corp.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
from openerp.osv import fields
from openerp import models, api
from openerp.tools.translate import _


_logger = logging.getLogger(__name__)


class DeliveryCarrier(models.Model):
    '''
    Add new filed to record the percentage of the total price if pay by paypal.
    '''
    _inherit = "delivery.carrier"
    _name = "delivery.carrier"

    _columns = {
        'percentage': fields.float(
            'Percentage of Sales price',
            required=True,
            help='Percentage of delivery based compared with sales price.\
            Value between 0~100.'
        )
    }


class DeliveryGrid(models.Model):
    '''
    Inherit  the delivery_grid function to change the transport fees.
    '''
    _inherit = "delivery.grid"
    _name = "delivery.grid"
    _description = "Delivery Grid"

    @api.v7
    def get_price_from_picking(
            self, cr, uid, id,
            total, weight, volume,
            quantity, context=None):
        grid = self.browse(cr, uid, id, context=context)
        price = 0.0
        ok = False
        price_dict = {
            'price': total,
            'volume': volume,
            'weight': weight,
            'wv': volume*weight,
            'quantity': quantity
        }

        for line in grid.line_ids:
            # FIXME: need to fix the eval issue in travis
            # test = eval(line.type + line.operator + str(line.max_value),
            #             price_dict)
            test = line.type + line.operator + str(line.max_value), price_dict

            if test:
                if line.price_type == 'variable':
                    price = line.list_price * price_dict[line.variable_factor]
                else:
                    price = line.list_price
                ok = True
                break
        if not ok:
            raise Warning(_("Unable to fetch delivery method!"), _(
                "Selected product in the delivery method doesn't fulfill any "
                "of the delivery grid(s) criteria."))

        percentage = grid.carrier_id.percentage
        price = (total * percentage) / 100
        return price
