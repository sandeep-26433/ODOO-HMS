from odoo import api, fields, models, _
from datetime import datetime

class AppointmentBooking(models.Model):
    _name = "appointment.booking"
    _description = "Appointment Booking"

    name = fields.Char(string="Patient Name")
    reference_id = fields.Char(string="Patient Reference ID")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ])
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age')
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    op_number = fields.Char(string="OP Number")

    department = fields.Selection([
        ('kayachikitsa', 'KAYACHIKITSA'),
        ('panchakarma', 'PANCHAKARMA'),
        ('streerogam_prasutitantra', 'STREEROGAM & PRASUTITANTRA'),
        ('kaumarabrityam', 'KAUMARABRITYAM'),
        ('shalyam', 'SHALAYAM'),
        ('shalakyam', 'SHALAKYAM'),
        ('swastavrittan', 'SWASTAVRITTAN'),
        ('emergency', 'EMERGENCY'),
        ('ip', 'IP'),
        ('counter_sales', 'COUNTER SALES')
    ], string="Department")

    consultation_doctor = fields.Many2one('consultation.doctor', string="Consultation Doctor")
    consultation_mode = fields.Selection([
        ('online', 'Online'),
        ('offline', 'Offline')
    ])
    if_online = fields.Text(string="If Online")
    referral = fields.Char(string="Referral(if Any)")
    priority = fields.Char(string="Priority")
    notes = fields.Text(string="Any Notes")

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = datetime.today()
                birth_date = fields.Date.from_string(record.date_of_birth)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                record.age = age
            else:
                record.age = 0

    @api.model
    def create(self, vals):
        """Automatically create a corresponding Doctor Appointment when a booking is made."""
        # Create the appointment booking record
        booking = super(AppointmentBooking, self).create(vals)

        # Automatically create a doctor.appointments record with mapped fields
        self.env['doctor.appointments'].create({
            'name': booking.name,  # Mapping Patient Name
            'reference_id': booking.reference_id,  # Mapping Reference ID
        })
        return booking
