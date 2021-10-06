# -*- coding: utf-8 -*-
from odoo import http

# class CrmClaimKanban(http.Controller):
#     @http.route('/crm_claim_kanban/crm_claim_kanban/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_claim_kanban/crm_claim_kanban/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_claim_kanban.listing', {
#             'root': '/crm_claim_kanban/crm_claim_kanban',
#             'objects': http.request.env['crm_claim_kanban.crm_claim_kanban'].search([]),
#         })

#     @http.route('/crm_claim_kanban/crm_claim_kanban/objects/<model("crm_claim_kanban.crm_claim_kanban"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_claim_kanban.object', {
#             'object': obj
#         })