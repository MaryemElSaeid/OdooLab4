from odoo import models, fields, api

class Order(models.Model):
    _name = 'itinew.order'
    _description = 'Description'

    name = fields.Char()
    date = fields.Date()
    model_2 = fields.One2many('itinew.basic.model2','order')
    partner = fields.Many2one('res.partner')
    timestamp = fields.Datetime()
    
    
    # price2 = fields.Float(compute="compute_value", store=True)

    # @api.onchange('unit_price')
    # def compute_value(self):
    #     for record in self:
    #         record.sub_total = record.unit_price * 5