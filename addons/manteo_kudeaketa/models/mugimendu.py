from odoo import fields, models


class ManteoMugimendu(models.Model):
    _name = 'manteo.mugimendu'
    _description = 'Gailu mugimendua'

    gailu_id = fields.Many2one('manteo.gailu', string='Gailua', required=True)
    gela_from_id = fields.Many2one('manteo.gela', string='Nondik')
    gela_to_id = fields.Many2one('manteo.gela', string='Nora')
    data = fields.Date(string='Data', default=fields.Date.context_today, required=True)
    arduraduna_id = fields.Many2one('res.users', string='Arduraduna')
    arrazoi = fields.Char(string='Arrazoia')
