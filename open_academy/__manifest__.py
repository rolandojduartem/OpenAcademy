{
    'name': 'Open Academy',
    'summary': """
        Odoo training""",
    'description': """
        Odoo training
    """,
    'application': True,
    'license': 'LGPL-3',
    'author': 'Odoo Community Association (OCA)',
    'website': 'https://github.com/rolandojduartem/OpenAcademy',
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'demo': [
        'demo/course.xml',
    ],
}
