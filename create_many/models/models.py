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
        partners = self.env["res.partner"].search([], limit=1000).ids
        teams = self.env["crm.team"].search([], limit=1000).ids
        stages = self.env["crm.stage"].search([], limit=1000).ids

        for i in range(10000):
            #per iteration
            day = randint(1, 27)
            month = randint(1, 12)
            year = randint(2010, date.today().year)
            self.env.cr.execute(f"""
                INSERT INTO crm_lead (
                    name,
                    partner_id,
                    expected_revenue,
                    create_date,
                    date_deadline,
                    date_closed,
                    team_id,
                    stage_id,
                    type,
                    active
                )
                VALUES (
                    '{"gen " + str(i) + "/" + str(uuid.uuid4())}',
                    {choice(partners)},
                    {randint(2000, 1000000)},
                    '{date(year, month, day)}',
                    '{date(year, month, day)}',
                    '{date(year, month, day)}',
                    {choice(teams)},
                    {choice(stages)},
                    'opportunity',
                    TRUE
                )
            """)
