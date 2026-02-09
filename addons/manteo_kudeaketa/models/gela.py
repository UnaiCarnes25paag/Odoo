from odoo import fields, models


class ManteoGela(models.Model):
    _name = 'manteo.gela'
    _description = 'Gela'

    name = fields.Char(string='Izena', required=True)
    kodea = fields.Char(string='Kodea')
    kokapena = fields.Char(string='Kokapena')
    oharrak = fields.Text(string='Oharrak')
    gailu_ids = fields.One2many('manteo.gailu', 'gela_id', string='Gailuak')
    ikasle_ids = fields.One2many('manteo.ikasle', 'gela_id', string='Ikasleak')
