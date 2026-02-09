from odoo import fields, models


class ManteoEsleipen(models.Model):
    _name = 'manteo.esleipen'
    _description = 'Gailu-esleipena'

    name = fields.Char(string='Erreferentzia', required=True, default='Esleipena')
    gailu_id = fields.Many2one('manteo.gailu', string='Gailua', required=True)
    ikasle_id = fields.Many2one('manteo.ikasle', string='Ikaslea', required=True)
    data_hasiera = fields.Date(string='Hasiera data', default=fields.Date.context_today, required=True)
    data_amaiera = fields.Date(string='Amaiera data')
    egoera = fields.Selection(
        [('aktibo', 'Aktibo'), ('itxita', 'Itxita')],
        string='Egoera',
        default='aktibo',
    )
    arduraduna_id = fields.Many2one('res.users', string='Arduraduna')
    oharra = fields.Text(string='Oharra')
