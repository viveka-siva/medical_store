from odoo import models, fields, api


class Medicines(models.Model):
    _name = 'product.medicine'
    name = fields.Char(string="Medicines Product")
    quantity = fields.Integer(string='Quantity')
    price = fields.Integer(string='Price')
    location = fields.Char(string='Location')
    # orderline = fields.One2many('order.line', 'orderlines_id', string='Orderline')

