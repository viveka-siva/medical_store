# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Medical Store',
    'version': '0.1',
    'summary': 'Whole Sale - Medical Store',
    'description': """ Mode Medical Store
    """,
    'depends': ['base'],
    'data': [
        'wizard/customer_details.xml',
        'security/ir.model.access.csv',
        'views/orderline.xml',
        'views/medicines.xml',
        'views/store_orders.xml',
    ],
    'installable': True,
    'auto_install': False
}