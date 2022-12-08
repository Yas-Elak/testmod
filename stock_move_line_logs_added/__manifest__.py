# -*- coding: utf-8 -*-
{
    'name': "stock_move_line_logs_added",

    'summary': """
        add logs for stock move line for an issue with amazon""",

    'description': """
         add logs for stock move line for an issue with amazon
    """,

    'author': "Odoo YLA",
    'website': "",
    'license': 'LGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product', 'barcodes','stock'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
}
