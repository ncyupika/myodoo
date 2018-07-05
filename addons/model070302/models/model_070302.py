# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions
from datetime import timedelta

class SafeReport(models.Model):
    _name = 'save.report'
    _rec_name = 'name'
    _description = 'New Description'

    house_address = fields.Char(string='房屋地址')
    name = fields.Char(string='地址')
    house_type = fields.Selection(selection=[(1,'透天'),(2,'大樓')],string='房屋類型')
    house_description = fields.Char(string='房屋介紹')
    house_about = fields.Char(string='關於')
    start_date = fields.Date(string='始租日期')
    duration = fields.Float(digits=(6, 0), help="租約期限")
    number_of_people = fields.Integer(string='居住人數')
    now_people = fields.One2many(comodel_name='students.management',inverse_name='currently_address')

class StudentsManagement(models.Model):
    _name = 'students.management'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char(string='姓名')
    sex_type = fields.Selection(selection=[(1,'男'),(2,'女')], string='生理性別')
    birthday = fields.Date(string='生日')
    info = fields.Char(string='身分證字號')
    currently_address = fields.Many2one('save.report',string='目前地址')
    ps = fields.Text('預約時間')
    student_introduce = fields.Char(string='自我介紹')
    student_about = fields.Char(string='學生評價')

    def book_time(self):
        return_date = datetime.date.today().strftime('%Y-%m-%d')
        self.ps = '我要預約' + return_date

class LandloreManadement(models.Model):
    _name = 'landlord.management'
    _rec_name = 'name'
    _description = 'New Description'

    name = fields.Char(string='姓名')
    phone_number = fields.Integer(string='市話')
    cellphone = fields.Integer(string='手機號碼')
    sex_type = fields.Selection(selection=[(1, '男'), (2, '女')], string='生理性別')
    birthday = fields.Date(string='生日')
    info = fields.Char(string='身分證字號')
    current_address = fields.Char(string='現居地址')





