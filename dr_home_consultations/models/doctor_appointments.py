from odoo import models, fields

class DoctorAppointments(models.Model):
    _name = "doctor.appointments"
    _description = "Doctor Appointments"

    name = fields.Char(string="Appointment Name")  # This will now store the Patient's Name
    reference_id = fields.Char(string="Patient Reference ID")  # New field to capture reference_id

    chief_complaint = fields.Text(string="Chief Complaint")
    associated_complaint = fields.Text(string="Associated Complaint")
    past_history = fields.Text(string="Past History")
    family_history = fields.Text(string="Family History")
    present_history = fields.Text(string="Present History")
    diagnosis = fields.Text(string="Diagnosis")
    investigations = fields.Text(string="Investigations")
    others = fields.Text(string="Others")
    artava = fields.Char(string="ARTAVA")
    nadi = fields.Char(string="NADI")
    agni = fields.Char(string="AGNI")
    mala = fields.Char(string="MALA")
    mutra = fields.Char(string="MUTRA")
    nidra = fields.Char(string="NIDRA")
    manas = fields.Char(string="MANAS")
    panchakarma_advice = fields.Text(string="Panchakarma Advice")
    htn = fields.Char(string="HTN")
    dm = fields.Char(string="DM")
    th = fields.Char(string="TH")
    prescribed_details = fields.Text(string="Prescription Details")

    # One2many field (kept in the model for data integrity)
    medicine_line_ids = fields.One2many('doctor.medicine.lines', 'appointment_id', string="Medicine Lines")

    def action_open_medicine_lines(self):
        self.ensure_one()
        action = self.env.ref('dr_home.action_doctor_medicine_lines').read()[0]
        action['domain'] = [('appointment_id', '=', self.id)]
        return action
