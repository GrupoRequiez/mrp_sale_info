# Copyright 2016 Antiun Ingenieria S.L. - Javier Iniesta
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "MRP Sale Info",
    "summary": "Adds sale information to Manufacturing models",
    "version": "14.0.0.0.1",
    "category": "Manufacturing",
    "website": "https://github.com/humanytek-team/mrp_sale_info",
    "author": "AvanzOSC, "
              "Tecnativa, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "depends": [
        "mrp",
        "sale_mrp",
        "stock",
        "sale_stock",
    ],
    "data": [
        "views/mrp_production.xml",
        "views/mrp_workorder.xml",
    ]
}
