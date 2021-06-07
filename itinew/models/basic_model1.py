from odoo import models, fields, api


class itinew(models.Model):
    _name = 'itinew.basic.model1'
    _description = 'itinew.itinew'

    name = fields.Char()
    price = fields.Integer()
    description = fields.Text()
    manufacturer = fields.Char()
    timestamp = fields.Datetime()
    model_2 = fields.One2many('itinew.basic.model2','model1')


    

   