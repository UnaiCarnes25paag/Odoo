{
    'name': 'Xabier-Zubiri-Manteo Kudeaketa',
    'version': '1.0',
    'summary': 'Ikastetxeko kudeaketa sistema',
    'description': """
Xabier-Zubiri-Manteo institutuarentzako
ikasle, irakasle eta ekipamenduen kudeaketa.
Gutxieneko funtzionalitateak: ikasleak, asistentziak,
kalifikazioak, gailuak, esleipenak eta gorabeherak.
    """,
    'author': 'Zure taldea',
    'category': 'Education',
    'depends': ['base', 'mail', 'website'],
    'data': [
        'security/groups.xml',
        'security/rules.xml',
        'security/ir.model.access.csv',
        'views/manteo_views.xml',
        'views/manteo_menus.xml',
        'views/website_templates.xml',
    ],
    'installable': True,
    'application': True,
}
