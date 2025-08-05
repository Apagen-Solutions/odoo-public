{
    'name': 'Highlight Mandatory Field',
    'version': '18.0.0.0',
    'category': 'Extra Tools',
    'summary': 'Personalize the styling of mandatory fields across Odoo form views.',
    'description': """This module applies a custom color to required fields in Odoo forms for better visual distinction""",
    'author': 'Apagen Solutions Pvt Ltd',
    'company': 'Apagen Solutions Pvt Ltd',
    'maintainer': 'Apagen Solutions Pvt Ltd',
    'website': 'https://www.apagen.com/',
    'depends': ['contacts', 'web'],
    'data': [
        'views/res_config_settings_views.xml',
        ],
    'assets': {
        'web.assets_backend': [
            'apg_mandatory_field_highlight/static/src/js/action_manager.js',
            'apg_mandatory_field_highlight/static/src/scss/field.scss',
        ],
    },

    'images': [
        'static/description/banner.jpg',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
