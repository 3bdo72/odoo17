{
    "name": "Real Estate",
    "summary": "Abdelrahman Real Estate",
    "description": """

        """,
    "author": "Abdelrahman Soliman",
    'category': 'Custom Modules/Backend',
    "sequence": '2',
    "website": "https://github.com/3bdo72",
    "version": "1.0.0",  # Valid version for Odoo 17.0.x.y or higher
    "license": "AGPL-3",
    "depends": ["base", "account", "sale_management", 'mail'],  # List dependent modules
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        
        "data/sequence.xml",
        
        "views/base_menu.xml",
        "views/property_view.xml",
        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
        "views/building_views.xml",
        "views/property_history_views.xml",
        "views/account_move_views.xml",
        
        "wizard/change_state_wizard_views.xml",
        
        "report/property_report.xml",
    ],
    "assets": {
        "web.assets_backend": ["app_one\static\src\css\property.css"],
        "web.report.assets_common": ["app_one/static/src/css/font.css"],
        },
    "application": True,
    "installable": True,
    "auto_install": False,
}
