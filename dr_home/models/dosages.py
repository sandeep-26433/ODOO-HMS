from odoo import models, fields

class DoctorDosages(models.Model):
    _name = 'doctor.dosages'
    _description = 'Dosages'

    dosage = fields.Char(string="Dosage")
