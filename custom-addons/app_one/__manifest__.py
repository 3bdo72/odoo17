{
    "name": "Real Estate",
    "summary": "Abdelrahman Real Estate",
    "description": """

        """,
    "author": "Abdelrahman Soliman",
    "website": "https://www.yourcompany.com",
    "version": "1.0.0",  # Valid version for Odoo 17.0.x.y or higher
    "category": "Sales",
    "license": "AGPL-3",
    "depends": ["base", "account", "sale_management", 'mail'],  # List dependent modules
    "data": [
        "security/ir.model.access.csv",
        "views/base_menu.xml",
        "views/property_view.xml",
        "views/owner_view.xml",
        "views/tag_view.xml",
        "views/sale_order_view.xml",
    ],
    "assets": {"web.assets_backend": ["app_one\static\src\css\property.css"]},
    "application": True,
    "installable": True,
    "auto_install": False,
}
