from odoo import api,fields,models
import urllib
import requests
import json
import ast

class whatsapp_link(models.TransientModel):
    _name = "whatsapp.link"
    _description = "Whatsapp link"

    name = fields.Char(string="Nombre")
    country = fields.Many2one('res.country', string="Pais", store=True)
    phone_number = fields.Char(string="Telefono")
    message = fields.Char(string="Mensaje Predeterminado")
    url = fields.Char(string="URL", compute="_generate_url", store=True)
    short_url = fields.Char(string="URL Corto", compute="_generate_short_url", store=True)

    @api.depends('name','country','phone_number','message')
    def _generate_url(self):
        for rec in self:
            if rec.name and rec.country and rec.phone_number and rec.message:
                formated_url = "https://api.whatsapp.com/send?phone=" + str(rec.country.num_code) + str(rec.phone_number) + "&text=" + urllib.quote(rec.message)
                rec.url = formated_url

    @api.depends('url')
    def _generate_short_url(self):
        url = "https://www.googleapis.com/urlshortener/v1/url"
        querystring = {"key":"AIzaSyBLCwJHqBKPH1isjD0E9vrhgzG_G1eDL3k"}

        for rec in self:
            payload = {"longUrl": rec.url}
            response = requests.request("POST", url, data=json.dumps(payload), headers = {'Content-Type': 'application/json'}, params=querystring)
            rec.short_url = ast.literal_eval(response.text)['id']
        
class res_contry(models.Model):
    _inherit = "res.country"
    _description = "Extend res.country"

    num_code = fields.Char(string="Codigo de Pais")
