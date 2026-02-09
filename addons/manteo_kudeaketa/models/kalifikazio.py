from odoo import fields, models


class ManteoKalifikazio(models.Model):
    _name = 'manteo.kalifikazio'
    _description = 'Kalifikazioa'

    ikasle_id = fields.Many2one('manteo.ikasle', string='Ikaslea', required=True)
    modulua = fields.Selection(
        [('ms', 'MS'), ('ssa', 'SSA'), ('wg', 'WG'), ('paag', 'PAAG')],
        string='Modulua',
        required=True,
    )
    ebaluazioa = fields.Selection(
        [('1', '1. ebaluazioa'), ('2', '2. ebaluazioa'), ('3', '3. ebaluazioa'), ('ekaina', 'Ekaina')],
        string='Ebaluazioa',
        required=True,
        default='1',
    )
    nota = fields.Float(string='Nota', required=True)
    irakasle_id = fields.Many2one('res.users', string='Irakaslea', required=True)
    oharrak = fields.Text(string='Oharrak')
