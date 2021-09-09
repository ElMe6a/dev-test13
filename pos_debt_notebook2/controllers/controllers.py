# -*- coding: utf-8 -*-
# from odoo import http


# class PosDebtNotebook(http.Controller):
#     @http.route('/pos_debt_notebook/pos_debt_notebook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_debt_notebook/pos_debt_notebook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_debt_notebook.listing', {
#             'root': '/pos_debt_notebook/pos_debt_notebook',
#             'objects': http.request.env['pos_debt_notebook.pos_debt_notebook'].search([]),
#         })

#     @http.route('/pos_debt_notebook/pos_debt_notebook/objects/<model("pos_debt_notebook.pos_debt_notebook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_debt_notebook.object', {
#             'object': obj
#         })
