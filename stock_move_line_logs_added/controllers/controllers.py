# -*- coding: utf-8 -*-
# from odoo import http


# class StockMoveLineLogsAdded(http.Controller):
#     @http.route('/stock_move_line_logs_added/stock_move_line_logs_added/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stock_move_line_logs_added/stock_move_line_logs_added/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stock_move_line_logs_added.listing', {
#             'root': '/stock_move_line_logs_added/stock_move_line_logs_added',
#             'objects': http.request.env['stock_move_line_logs_added.stock_move_line_logs_added'].search([]),
#         })

#     @http.route('/stock_move_line_logs_added/stock_move_line_logs_added/objects/<model("stock_move_line_logs_added.stock_move_line_logs_added"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stock_move_line_logs_added.object', {
#             'object': obj
#         })
