
{
    'name': "ToDo",
    'summary': "ToDo App Training",
    'description': """
ToDo Task to Apply for all the previous videos of the odoo playlist
    """,
    'author': "Abdel-Rahman Soliman",
    'category': 'Administration',
    'version': '0.1',
    "license": "AGPL-3",
    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/base_menu.xml",
        "views/todo_task_views.xml"
    ],
    "application": True,
    "installable": True,
}

