from odoo import models, fields

class DoctorMedicines(models.Model):
    _name = 'doctor.medicines'
    _description = 'Medicines'

    medicine_name = fields.Char(string="Medicine Name")
