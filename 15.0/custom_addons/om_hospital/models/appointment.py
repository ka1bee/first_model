from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    gender = fields.Selection(related='patient_id.gender')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')

    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")

