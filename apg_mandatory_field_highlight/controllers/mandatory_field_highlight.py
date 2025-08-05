
from odoo import http
from odoo.http import request


class MandatoryFieldSettings(http.Controller):
    """Controller to return the method of values from config settings."""

    @http.route('/mandatory/config_params', type='json', auth="public")
    def website_get_config_value(self):
        """Returning the values from config settings to js"""
        get_param = request.env['ir.config_parameter'].sudo().get_param
        return {
            'margin_left_color': get_param(
                'apg_mandatory_field_highlight.margin_left_color'),
            'margin_right_color': get_param(
                'apg_mandatory_field_highlight.margin_right_color'),
            'margin_top_color': get_param(
                'apg_mandatory_field_highlight.margin_top_color'),
            'margin_bottom_color': get_param(
                'apg_mandatory_field_highlight.margin_bottom_color'),
            'field_background_color': get_param('apg_mandatory_field_highlight'
                                                '.field_background_color')
        }
