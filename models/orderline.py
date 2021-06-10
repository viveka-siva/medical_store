from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Orderlines(models.Model):
    _name = 'order.line'
    quantity = fields.Integer(string='Quantity')
    unit_price = fields.Integer(string='Unit Price')
    total = fields.Integer('Total', required=True)
    product_id = fields.Many2one('product.medicine', string='Product')
    orderlines_id = fields.Many2one('market.order', string='Order')