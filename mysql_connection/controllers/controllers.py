# -*- coding: utf-8 -*-
from odoo import http

# class MysqlConnection(http.Controller):
#     @http.route('/mysql_connection/mysql_connection/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mysql_connection/mysql_connection/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mysql_connection.listing', {
#             'root': '/mysql_connection/mysql_connection',
#             'objects': http.request.env['mysql_connection.mysql_connection'].search([]),
#         })

#     @http.route('/mysql_connection/mysql_connection/objects/<model("mysql_connection.mysql_connection"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mysql_connection.object', {
#             'object': obj
#         })