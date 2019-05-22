# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Formulario Ausencia',
    'category': 'Website',
    'summary': 'Build custom web forms',
    'version': '1.0',
    'description': """
Customize and create your own web forms.
This module adds a new building block in the website builder in order to build new forms from scratch in any website page.
    """,
    'depends': ['base', 'website', 'hr_holidays', 'website_enterprise', 'website_form',],
    'data': [
        'views/snippets.xml',
        'views/ir_model_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'OEEL-1',
}
