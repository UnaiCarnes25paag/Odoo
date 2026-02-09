from odoo import fields, models


class ManteoGailu(models.Model):
    _name = 'manteo.gailu'
    _description = 'Gailu informatikoa'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Izena', required=True, tracking=True)
    seriea = fields.Char(string='Serie zenbakia', tracking=True)
    mota = fields.Selection(
        [
            ('pc', 'Ordenagailu estatikoa'),
            ('laptop', 'Eramangarria'),
            ('pantaila', 'Pantaila'),
            ('periferiko', 'Periferikoa'),
            ('beste', 'Beste bat'),
        ],
        string='Mota',
        required=True,
        tracking=True,
    )
    egoera = fields.Selection(
        [
            ('operatibo', 'Operatibo'),
            ('matxuratuta', 'Matxuratuta'),
            ('konpontzen', 'Konpontzen'),
            ('baja', 'Baja'),
        ],
        string='Egoera',
        default='operatibo',
        tracking=True,
    )
    gela_id = fields.Many2one('manteo.gela', string='Uneko gela', tracking=True)
    ikasle_id = fields.Many2one('manteo.ikasle', string='Esleitutako ikaslea', tracking=True)
    esleipen_ids = fields.One2many('manteo.esleipen', 'gailu_id', string='Esleipen historikoa')
    gorabehera_ids = fields.One2many('manteo.gorabehera', 'gailu_id', string='Gorabeherak')
    mugimendu_ids = fields.One2many('manteo.mugimendu', 'gailu_id', string='Mugimenduak')
    erosketa_id = fields.Many2one('manteo.erosketa', string='Erosketa eskaera')
    prezioa = fields.Float(string='Erosketa prezioa')
    ohar_teknikoak = fields.Text(string='Ohar teknikoak')

*** End of File
