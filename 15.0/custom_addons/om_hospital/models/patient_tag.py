from odoo import api, fields, models


class PatientTag(models.Model):
    _name = "patient.tag"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Patient Tag"

    name = fields.Char(string='Name', required=True)
    active = fields.Boolean(string='Active', default=True)
