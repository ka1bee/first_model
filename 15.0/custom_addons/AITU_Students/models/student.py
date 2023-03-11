from odoo import api, fields, models
from datetime import date


class Student(models.Model):
    _name = "aitu.student"
    _description = "AITU Student"

    name = fields.Char(string='Name')
    age = fields.Integer(string="Age")
    course = fields.Integer(string="Course")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
