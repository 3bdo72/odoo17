# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",
    'summary': "We Are Here To Help You",
    'description': """
    Whenever You Need Help, We Are Here To Help.
    """,
    'author': "Abdel-Rahman Soliman",
    'website': "https://github.com/3bdo72",
    'category': 'Custom Modules/Backend',
    'version': '0.1',
    'sequence': '-11',
    "application": True,
    "installable": True,

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'hr', 'calendar'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/base.xml",
        "views/hospital_patient_views.xml",
        "views/patient_gender_view.xml",
        "views/hospital_appointment_views.xml",
        "views/hospital_doctor_views.xml"
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

