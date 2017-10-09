# -*- coding: utf-8 -*-
from odoo import api,fields,models

class bot_messenger(models.Model):
    _name = "bot.messenger"
    _description = "Bot Messenger"

    name = fields.Char(string="Nombre del Bot")
    page_id = fields.Char(string="Page ID")
    page_token = fields.Char(string="Page Access Token")

class bot_messenger_contact(models.Model):
    _name = "bot.messenger.contact"
    _description = "Bot Messenger Contact"

    name = fields.Char(u"Nombre")
    identifier = fields.Char(u"Identificador")
    bot_id = fields.Many2one(
        'bot.messenger', string='Bot Asociado',
        ondelete='cascade', required=True, default=lambda self: self.env['bot.messenger'].search([], limit=1, order='id desc'))