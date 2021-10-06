# -*- coding: utf-8 -*-
{
    'name': "Claim Management Kanban",

    'summary': """
        Extend the crm_clain module with a kanban view""",

    'description': """
        Extend the crm_clain module with a kanban view
    """,

    'author': "Alberto Carollo",
    'website': "https://github.com/baba75/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customer Relationship Management',
    'version': '12.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','crm','crm_claim'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],

}