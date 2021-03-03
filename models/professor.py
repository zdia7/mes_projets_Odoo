# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
     _name = 'university.professor'

     first_name = fields.Char('First name')
     last_name = fields.Char('Last name')
     sexe = fields.Selection([('male', 'Male'), ('female', 'Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Adress')
     birthday = fields.Date('Birthday')
     start_date = fields.Datetime('Start date')

     department_id = fields.Many2one(comodel_name='university.departement')

     subject_id = fields.Many2one(comodel_name='university.subject')

     classroom_id = fields.Many2many(comodel_name='university.classroom',
     								 relation = 'prof_class_rel')