# -*- coding: utf-8 -*-
from odoo import api,fields,models
import requests
import json

class bot_quick_send_wizard(models.TransientModel):
    _name = "bot.quick_send_wizard"
    _description = "Envio rapido"

    name = fields.Char(u"Identificador de envío")
    text = fields.Text("Texto")
    bot_id = fields.Many2one(
        'bot.messenger', string='Bot Messenger',
        ondelete='cascade', required=False, default=lambda self: self.env['bot.messenger'].search([], limit=1, order='id desc'))

    @api.multi
    def send_messages(self):
        # Sms = self.env["sms.sms"]
        dests = []
        if self.bot_id:
            for x in self.env["bot.messenger.contact"].search([('bot_id','=',self.bot_id.id)]):
                dests.append(x.identifier)

        if len(dests) >= 1:
            # POST -> https://edb14610.ngrok.io/messenger/send_messages <- Cambiar dominio
            # {"messenger": {"ids": dests, "text": self.text} }

            url = self.env["ir.config.parameter"].get_param("send.messages")
            response = requests.request("POST", url, data=json.dumps({"messenger": {"ids": dests, "text": self.text} }), headers = {'Content-Type': 'application/json'})
            print(response.text)

        return {
            'name': 'Bot Messenger',
            'res_model': 'bot.messenger',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'list,form',
        }
