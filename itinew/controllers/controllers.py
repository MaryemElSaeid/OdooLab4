# -*- coding: utf-8 -*-
from odoo import http


class Itinew(http.Controller):
    @http.route('/itinew/itinew/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/itinew/itinew/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('itinew.listing', {
            'root': '/itinew/itinew',
            'objects': http.request.env['itinew.itinew'].search([]),
        })

    @http.route('/itinew/itinew/objects/<model("itinew.itinew"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('itinew.object', {
            'object': obj
        })

