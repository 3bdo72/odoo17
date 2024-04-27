# -*- coding: utf-8 -*-
{
    "name": "Book Store",
    "summary": "Abdelrahman Book Store",
    "description": """
We Sell Toys, Books, Gifts and Print whatever u want
    """,
    "author": "Abdelrahman Soliman",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sales",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        # "views/views.xml",
        # "views/templates.xml",
        "views/base_menu.xml",
        "views/books.xml",
        "views/toys.xml",
        "views/customer_order.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
    # Assets definition
    "assets": {
        "web.assets_backend": [
            "your_module/static/src/js/toggle_widget.js",
            "your_module/static/src/xml/toggle_widget_template.xml",
        ],
    },
}
