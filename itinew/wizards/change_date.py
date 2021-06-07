from odoo import models, fields, api

class ChangeDateWizard(models.TransientModel):
    _name = 'itinew.change.date.wizard'
    _description = 'Description'
    

    def action_change_date(self):
        self.ensure_one()
        active_id = self.env['itinew.order'].browse(self._context.get('active_id')).copy()
      
        # active_id.write({'timestamp': self.date})
        # data = self.read(cr, uid, ids)[0]
        # article_id = context['active_id']

        # vals = {
        #     'name':self.name,
        #     'date':self.date
        # }
        # print("vals.....",vals)


        # def duplicate_object(self, cr, uid, ids, context=None):

