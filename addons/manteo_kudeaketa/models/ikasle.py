from odoo import fields, models


class ManteoIkasle(models.Model):
    _name = 'manteo.ikasle'
    _description = 'Ikaslea'

    name = fields.Char(string='Izena', required=True)
    abizenak = fields.Char(string='Abizenak')
    email = fields.Char(string='Posta korporatiboa')
    telefonoa = fields.Char(string='Telefonoa')
    ikasmaila = fields.Selection(
        [
            ('ms', 'MS'),
            ('ssa', 'SSA'),
            ('wg', 'WG'),
            ('paag', 'PAAG'),
        ],
        string='Ikasmaila',
        required=True,
    )
    ikasturtea = fields.Selection(
        [('1', '1. maila'), ('2', '2. maila')],
        string='Ikasturtea',
        default='1',
    )
    user_id = fields.Many2one('res.users', string='Erabiltzailea', help='Portal edo barne erabiltzailea')
    gela_id = fields.Many2one('manteo.gela', string='Gela')
    esleipen_ids = fields.One2many('manteo.esleipen', 'ikasle_id', string='Esleipenak')
    asistentzia_ids = fields.One2many('manteo.asistentzia', 'ikasle_id', string='Asistentziak')
    kalifikazio_ids = fields.One2many('manteo.kalifikazio', 'ikasle_id', string='Kalifikazioak')
    gorabehera_ids = fields.One2many('manteo.gorabehera', 'ikasle_id', string='Gorabeherak')
    active = fields.Boolean(default=True, string='Aktibo')
*** End of File
