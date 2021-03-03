# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityClassroom(models.Model):
     _name = 'university.classroom'

     classroom_name = fields.Char(String='name')
     code = fields.Char()

     university_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')

     professor_id = fields.Many2many(comodel_name='university.professor',
     								 relation = 'class_prof_rel')

     subject_id = fields.Many2many(comodel_name='university.subject',
     								 relation = 'class_sub_rel')
     
     