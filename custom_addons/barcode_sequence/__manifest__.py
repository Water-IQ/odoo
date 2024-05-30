# -*- coding: utf-8 -*-
{
    "name": "barcode_sequence",
    "summary": "Auto increment barcode sequence",
    "description": """
        Auto increment barcode number by x whenever a new product is added to inventory.
    """,
    "author": "WaterIQ Technologies",
    "website": "https://www.yourcompany.com",
    "category": "Custom",
    "version": "1.0",
    # any module necessary for this one to work correctly
    "depends": ["base", "web"],
    # always loaded
    "data": [
        "views/views.xml",
    ],
}
