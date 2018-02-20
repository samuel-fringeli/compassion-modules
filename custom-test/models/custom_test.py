from odoo import models, fields, api


class CustomTest(models.Model):
    _name = 'custom.test'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done ?')
    active = fields.Boolean('Active ?', default=True)

    @api.one
    def do_toggle_done(self):
        self.is_done = not self.is_done

    @api.multi
    def do_clear_done(self):
        self.search([('is_done', '=', True)]).write({'active': False})
        return True
