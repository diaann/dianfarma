# -*- coding: utf-8 -*-
# from odoo import http


# class Dianfarma(http.Controller):
#     @http.route('/dianfarma/dianfarma', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dianfarma/dianfarma/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dianfarma.listing', {
#             'root': '/dianfarma/dianfarma',
#             'objects': http.request.env['dianfarma.dianfarma'].search([]),
#         })

#     @http.route('/dianfarma/dianfarma/objects/<model("dianfarma.dianfarma"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dianfarma.object', {
#             'object': obj
#         })
