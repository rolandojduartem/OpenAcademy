{
    'name': 'Open Academy',
    'summary': """
        Odoo training""",
    'application': True,
    'license': 'LGPL-3',
    'author': 'Odoo Community Association (OCA)',
    'website': 'https://github.com/rolandojduartem/OpenAcademy',
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    'depends': ['base'],
    'data': [
        'data/res_group.xml',
        'security/ir.model.access.csv',
        'views/partner.xml',
        'views/course.xml',
        'views/session.xml',
        'data/ir_ui_menu.xml',
    ],
    'demo': [
        'demo/category.xml',
        'demo/res_partner.xml',
        'demo/res_users.xml',
        'demo/course.xml',
        'demo/session.xml',
    ],
}
