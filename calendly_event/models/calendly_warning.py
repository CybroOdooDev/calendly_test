from odoo import api, fields, models


class CalendlyWarning(models.TransientModel):
    _name = 'calendly.warning'
    _description = 'Calendly Warning wizard'

    message = fields.Text(string="It will remove already existing calendly api, And create new one with this api key",
                          readonly=True, store=True)
