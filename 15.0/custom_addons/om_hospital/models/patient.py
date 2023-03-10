from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string='Name')
    last_name = fields.Char(string='Last Name')
    full_name = fields.Char(string="Full Name", compute='_compute_full_name')
    date_of_birth = fields.Date('Date Of Birth')
    ref = fields.Char(string='Reference')
    age = fields.Integer(string="Age", compute='_compute_age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    tag_ids = fields.Many2many('patient.tag', string="Tags")



    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.name} {rec.last_name}"

    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year-rec.date_of_birth.year
            else:
                rec.age = 0

