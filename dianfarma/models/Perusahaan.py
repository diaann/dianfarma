from odoo import api, fields, models


class Perusahaan(models.Model):
    _name = 'dianfarma.perusahaan'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    produk_ids = fields.One2many(
        comodel_name='dianfarma.produk', 
        inverse_name='perusahaan_id', 
        string='Produk')
    
