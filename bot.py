# -*- coding: utf-8 -*-
from odoo import api,fields,models

class bot_messenger(models.TransientModel):
    _name = "bot.messenger"
    _description = "Bot Messenger"

    name = fields.Char(string="Nombre del Bot")

class bot_messenger_contact(models.TransientModel):
    _name = "bot.messenger.contact"
    _description = "Bot Messenger Contact"

    name = fields.Char(u"Nombre")
    identifier = fields.Char(u"Identificador")
    bot_id = fields.Many2one(
        'bot.messenger', string='Bot Asociado',
        ondelete='cascade', required=True, default=lambda self: self.env['bot.messenger'].search([], limit=1, order='id desc'))