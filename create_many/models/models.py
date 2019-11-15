# -*- coding: utf-8 -*-

from odoo import models, fields, api
from random import choice, randint
from datetime import date

# class create_many(models.Model):
#     _name = 'create_many.create_many'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Lead(models.Model):
    _inherit = 'crm.lead'


    def action_populate(self):
        #once
        import uuid
        partners = self.env["res.partner"].search_read(fields=["id"],limit=1000)
        teams = self.env["crm.team"].search_read(fields=["id"], limit=1000)

        for i in range(1000):
            #per iteration
            day = randint(1,27)
            month = randint(1,12)
            year = randint(2010,date.today().year)
            created = self.env['crm.lead'].create({
                "name": "gen "+ str(i) + "/" + str(uuid.uuid4()),
                "partner_id": choice(partners)["id"],
                "planned_revenue": randint(2000,1000000),
                "create_date": date(year,month,day),
                "team_id": choice(teams)["id"],
            })
            updateDate = """update crm_lead set create_date = '%s' where id = %s"""%(date(year, month,day), created.id)
            self.env.cr.execute(updateDate)
