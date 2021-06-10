from odoo import models, fields, api


class OrderList(models.Model):
    _name = 'medicine.order'

    name = fields.Char(string='Customer Name:')
    order_date = fields.Date(string='Ordered Date:')
    total = fields.Integer(string='Total')
    orderlist_ids = fields.One2many('order.line', 'orderlines_id', string="Product List")
    gst_number = fields.Char(string="GST Number:")
    address_info = fields.Text(string="Address")
    state_info = fields.Char(string='State')
    city_info = fields.Char(string='City')
    aadhar = fields.Integer('Aadhar Card No.:')
    pan = fields.Char('PanCard No.:')

    def calculate_total(self):
        sum = 0
        for rec in self.orderlist_ids:
            sum += rec.total
            self.write({'total': sum})
        return True