# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
     _name = 'university.student'

     first_name = fields.Char('First name')
     last_name = fields.Char('Last name')
     sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Adress')
     birthday = fields.Date('Birthday')
     registration_date = fields.Date('Registration date')

     department_id = fields.Many2one(comodel_name='university.department')
     
     classroom_id = fields.Many2one(comodel_name='university.classroom')