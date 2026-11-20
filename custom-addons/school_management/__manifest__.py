{
    'name': 'School Management',
    'version': '17.0.1.0.0',
    'summary': 'Core module for School Management ERP',
    'description': """
        School Management ERP System.
        Core module for managing school data.
    """,
    'author': 'Abdelrahman Soliman',
    'category': 'Education',
    'license': 'LGPL-3',
    'sequence': '-13',
    'depends': [
        'base',
    ],

    "data": [
        "security/ir.model.access.csv",
        "views/base_menu.xml",
        "views/school_student_views.xml",
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
