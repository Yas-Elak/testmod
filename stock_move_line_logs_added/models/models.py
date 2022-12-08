# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)


class stock_move_line_logs_added(models.Model):
    _inherit = 'stock.move.line'

    def _action_done(self):

        for ml in self:
            _logger.warning("Stock move line start")
            _logger.warning(ml.id)
            _logger.warning(ml.picking_id)
            _logger.warning(ml.move_id)
            _logger.warning(ml.product_id)
            _logger.warning(ml.package_id)
            _logger.warning(ml.lot_id)
            _logger.warning(ml.lot_name)
            _logger.warning(ml.location_id)
            _logger.warning(ml.location_dest_id)
            _logger.warning(ml.reference)
            _logger.warning("Stock move line end")

            res = super(stock_move_line_logs_added, self)._action_done(self)
            return res
