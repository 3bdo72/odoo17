# -*- coding: utf-8 -*-
{
    "name": "Book Store",
    "summary": "Abdelrahman Book Store",
    "description": """
We Sell Toys, Books, Gifts and Print whatever u want
    """,
    "author": "Abdelrahman Soliman",
    "website": "https://www.yourcompany.com",
    "category": "Services",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/base_menu.xml",
        "views/books.xml",
        "views/toys.xml",
        "views/customer_order.xml",
        "views/fiction_views.xml",
        "views/action_views.xml",
        "views/drama_views.xml",
        "views/transaction_history_views.xml"
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,

}
