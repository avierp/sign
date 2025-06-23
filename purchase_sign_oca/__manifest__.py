# Copyright 2025 Aviseo - Tyler Sampson
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Purchase Sign Oca",
    "version": "17.0.1.0.0",
    "category": "Purchase",
    "website": "https://github.com/OCA/sign",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["sign_oca", "purchase"],
    "data": [
        "views/purchase_order_views.xml",
        "views/sign_oca_request_views.xml",
    ],
    "demo": [
        # "demo/sign_oca_role.xml",
        # "demo/sign_oca_template.xml",
    ],
    "installable": True,
    "maintainers": ["tylersampson"],
}
