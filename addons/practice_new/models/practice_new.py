# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
     _name = 'openacademy.course'

     name = fields.Char(string="標題", required=True)
     description = fields.Text()

     responsible_id = fields.Many2one('res.users', ondelete='set null', string="主管", index=True)
     session_ids = fields.One2many('openacademy.session', 'course_id', string="會議")


class Session(models.Model):
     _name = 'openacademy.session'

     name = fields.Char(required=True, string="主題")
     start_date = fields.Date(string="開始日期")
     duration = fields.Float(digits=(6, 2), help="Duration in days", string="持續時間")
     seats = fields.Integer(string="座位數量")

     instructor_id = fields.Many2one('res.partner', string="講師", domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")])
     course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="課程", required=True)
     attendee_ids = fields.Many2many('res.partner', string="與會者")