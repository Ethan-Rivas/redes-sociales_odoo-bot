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
    url = fields.Char(string="URL", compute="_generate_url")
    short_url = fields.Char(string="URL Corto", compute="_generate_short_url")

    @api.model
    def _generate_url(self):
        formated_url = "https://api.whatsapp.com/send?phone=" + str(self.country.num_code) + str(self.phone_number) + "&text=" + urllib.quote(self.message)
        print(formated_url)

        self.url = formated_url

    @api.model
    def _generate_short_url(self):
        url = "https://www.googleapis.com/urlshortener/v1/url"
        querystring = {"key":"AIzaSyDk-K2QC_NNiguHScCsnfGT784RvrMpbQI"}
        payload = {"longUrl": self.url}

        response = requests.request("POST", url, data=json.dumps(payload), headers = {'Content-Type': 'application/json'}, params=querystring)
        self.short_url = ast.literal_eval(response.text)['id']
        
class res_contry(models.Model):
    _inherit = "res.country"
    _description = "Extend res.country"

    num_code = fields.Char(string="Codigo de Pais")
