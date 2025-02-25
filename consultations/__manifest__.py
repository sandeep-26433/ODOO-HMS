{
    'name': 'Appointment Booking',
    'version': '17.0',
    'summary': 'Consultations Module',
    'sequence': 10,
    'description': """Appointments Booking""",
    'category': 'Hospital Management',
    'website': '',
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/appointment_booking.xml',
        'views/consultation_doctor.xml'
    ],

    'demo': [],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}
