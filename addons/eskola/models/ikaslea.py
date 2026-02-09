from odoo import models, fields

class EskolaIkaslea(models.Model):
    _name = 'eskola.ikaslea'
    _description = 'Ikaslea'

    name = fields.Char(string='Izena', required=True)
    surname = fields.Char(string='Abizena')
    image = fields.Image(string='Irudia')

    student_age = fields.Integer(string='Adina')
    student_day_of_birth = fields.Date(string='Jaiotze data')

    student_gender = fields.Selection(
        [
            ('m', 'Male'),
            ('f', 'Female'),
            ('o', 'Other'),
        ],
        string='Generoa'
    )

    student_blood_group = fields.Selection(
        [
            ('A+', 'A+ve'),
            ('B+', 'B+ve'),
            ('O+', 'O+ve'),
            ('AB+', 'AB+ve'),
            ('A-', 'A-ve'),
            ('B-', 'B-ve'),
            ('O-', 'O-ve'),
            ('AB-', 'AB-ve'),
        ],
        string='Odol taldea'
    )
