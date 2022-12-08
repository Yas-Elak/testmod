# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)


class stock_move_line_logs_added(models.Model):
    _inherit = 'stock.move.line'

    def _action_done(self):

        for ml in self:
            _logger.warning("Stock move line start")
            _logger.warning(str(ml.id) + " ml.id")
            _logger.warning(str(ml.picking_id) + " ml.picking_id")
            _logger.warning(str(ml.move_id) + "ml.move_id")
            _logger.warning(str(ml.move_id.picking_type_id) + "ml.")
            _logger.warning(str(ml.move_id.picking_type_id.use_create_lots) + "ml.move_id.picking_type_id.use_create_lots")
            _logger.warning(str(ml.product_id) + "ml.product_id")
            _logger.warning(str(ml.product_id.tracking) + "ml.product_id.tracking")
            _logger.warning(str(ml.package_id) + "ml.package_id")
            _logger.warning(str(ml.lot_id) + "ml.lot_id")
            _logger.warning(str(ml.lot_name) + "ml.lot_name")
            _logger.warning(str(ml.location_id) + "ml.location_id")
            _logger.warning(str(ml.location_dest_id) + "ml.location_dest_id")
            _logger.warning(str(ml.reference) + "ml.reference")
            _logger.warning("Stock move line end")

            res = super(stock_move_line_logs_added, self)._action_done()
            return res