from odoo import fields, models


class ManteoAsistentzia(models.Model):
    _name = 'manteo.asistentzia'
    _description = 'Ikaslearen asistentzia'

    ikasle_id = fields.Many2one('manteo.ikasle', string='Ikaslea', required=True)
    data = fields.Date(string='Data', required=True, default=fields.Date.context_today)
    egoera = fields.Selection(
        [('etorri', 'Etorri'), ('huts', 'Ez da etorri'), ('berandu', 'Berandu')],
        string='Egoera',
        required=True,
        default='etorri',
    )
    irakasle_id = fields.Many2one('res.users', string='Irakaslea', required=True)
    oharrak = fields.Text(string='Oharrak')
