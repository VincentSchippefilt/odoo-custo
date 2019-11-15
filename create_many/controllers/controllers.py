# -*- coding: utf-8 -*-
from odoo import http

# class CreateMany(http.Controller):
#     @http.route('/create_many/create_many/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_many/create_many/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_many.listing', {
#             'root': '/create_many/create_many',
#             'objects': http.request.env['create_many.create_many'].search([]),
#         })

#     @http.route('/create_many/create_many/objects/<model("create_many.create_many"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_many.object', {
#             'object': obj
#         })