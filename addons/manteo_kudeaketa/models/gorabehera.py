from odoo import fields, models


class ManteoGorabehera(models.Model):
    _name = 'manteo.gorabehera'
    _description = 'Gorabehera teknikoa'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Izenburua', required=True, tracking=True)
    gailu_id = fields.Many2one('manteo.gailu', string='Gailua', tracking=True)
    ikasle_id = fields.Many2one('manteo.ikasle', string='Ikaslea', tracking=True)
    egoera = fields.Selection(
        [
            ('irekita', 'Irekita'),
            ('lanean', 'Lanean'),
            ('konponduta', 'Konponduta'),
            ('baztertuta', 'Baztertuta'),
        ],
        string='Egoera',
        default='irekita',
        tracking=True,
    )
    lehentasuna = fields.Selection(
        [('txikia', 'Txikia'), ('ertaina', 'Ertaina'), ('larria', 'Larria')],
        string='Lehentasuna',
        default='ertaina',
        tracking=True,
    )
    arduraduna_id = fields.Many2one('res.users', string='Mantentze arduraduna', tracking=True)
    data_ireki = fields.Date(string='Irekiera data', default=fields.Date.context_today)
    data_itxi = fields.Date(string='Itxiera data')
    deskribapena = fields.Text(string='Deskribapena')
    oharrak = fields.Text(string='Ohar gehigarriak')
