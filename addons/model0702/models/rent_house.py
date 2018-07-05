# -*- coding: utf-8 -*-
from odoo import models, fields, api
import datetime

class RentHouse(models.Model):
    _name = 'rent.house'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char(string='地址')
    master = fields.Char(string='房東')
    title = fields.Char(string='房屋標題')
    house_id = fields.One2many(comodel_name='own.system',inverse_name='person_id')
    house_type = fields.Selection(selection=[(1,'透天'),(2,'大樓')],string='房屋類型')

class Master(models.Model):
    _name = 'master'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char(string='姓名')
    name_info = fields.Char(string='身分證字號')

class OwnSystem(models.Model):
    _name = 'own.system'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char('標題', compute='rent_default_name')
    person_id = fields.Many2one(comodel_name='master', string='房東')
    house_id = fields.Many2one(comodel_name='rent.house',string='擁有房屋')
    ps = fields.Text('備註')
    def rent_over(self):
        return_date = datetime.date.today().strftime('%Y-%m-%d')
        self.ps = '我要出租' + return_date

    @api.depends('person_id', 'house_id')
    def rent_default_name(self):
        for line in self:
            if line.person_id and line.house_id :
                line.name = line.house_id.name + line.person_id.name

