from odoo import fields, models


class ManteoErosketa(models.Model):
    _name = 'manteo.erosketa'
    _description = 'Erosketa eskaera'

    name = fields.Char(string='Erreferentzia', required=True, default='Erosketa eskaera')
    mota = fields.Selection(
        [
            ('pc', 'Ordenagailua'),
            ('pantaila', 'Pantaila'),
            ('periferiko', 'Periferikoa'),
            ('beste', 'Beste bat'),
        ],
        string='Ekipamendu mota',
        required=True,
    )
    kantitatea = fields.Integer(string='Kantitatea', default=1, required=True)
    gela_id = fields.Many2one('manteo.gela', string='Helmuga gela')
    egoera = fields.Selection(
        [
            ('zain', 'Zain'),
            ('onartua', 'Onartua'),
            ('eskatuta', 'Eskatuta'),
            ('jasota', 'Jasota'),
            ('baztertuta', 'Baztertuta'),
        ],
        string='Egoera',
        default='zain',
    )
    eskatzailea_id = fields.Many2one('res.users', string='Eskatzailea', required=True)
    kostua_estimatua = fields.Float(string='Kostu estimatua')
    oharrak = fields.Text(string='Oharrak')
