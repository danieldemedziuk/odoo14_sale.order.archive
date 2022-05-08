# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class SaleOrderArchive(models.Model):
    _name = 'sale.order.archive'
    _description = "Sale order archive"

    name = fields.Char(string='Name')
    create_date = fields.Date(string='Creation date')
    customer_id = fields.Many2one('res.partner', string='Customer')
    sale_person_id = fields.Many2one('res.users', string='Sale person')
    total_amount = fields.Monetary(string='Total amount')
    currency_id = fields.Many2one('res.currency', string='Currency')
    count_order_lines = fields.Integer(string='Order lines')

    @api.model
    def cron_archive(self):
        today = datetime.today().date()
        week_ago = today - timedelta(days=7)

        for rec in self.env['sale.order'].search([('create_date', '<', week_ago)]):
            if rec:
                self.env['sale.order.archive'].create({
                    'name': rec['name'],
                    'create_date': rec['create_date'],
                    'customer_id': rec['partner_id']['id'],
                    'sale_person_id': rec['user_id']['id'],
                    'total_amount': rec['amount_total'],
                    'currency_id': rec['currency_id']['id'],
                    'count_order_lines': len(rec['order_line'])
                })

                rec['state'] = 'cancel'
                rec.unlink()
