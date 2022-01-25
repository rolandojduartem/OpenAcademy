from odoo import http


class DashboardController(http.Controller):
    """ This controller was created to fix the custom_id error that
        appeared when the user try to move the dashboard elements """
    @http.route('/web/view/edit_custom', type='json', auth="user")
    def edit_custom(self, arch):
        return {'result': True}
