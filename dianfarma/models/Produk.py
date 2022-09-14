from odoo import api, fields, models


class Produk(models.Model):
    _name = 'dianfarma.produk'
    _description = 'New Description'
    
    name = fields.Char(
        string='Nama Produk',
        required=True)
    kategoriproduk_id = fields.Many2one(
        comodel_name='dianfarma.kategoriproduk',
        string='Kategori Produk',
        ondelete='cascade')
    jenisobat_id = fields.Many2one(
        comodel_name='dianfarma.jenisobat',
        string='Jenis Obat',
        ondelete='cascade')
    harga_beli = fields.Integer(
        string='Harga Beli',
        required=True)
    harga_jual = fields.Integer(
        string='Harga Jual',
        required=True)
    no_izin = fields.Char(string='Nomor Izin Edar')
    stok = fields.Integer(string='Stok')
    perusahaan_id = fields.Many2one(
        comodel_name='dianfarma.perusahaan', 
        string='Produsen',
        ondelete='cascade')
    golongan_id = fields.Many2one(
        comodel_name='dianfarma.golonganobat', 
        string='Golongan Obat')
    image = fields.Image('Gambar Produk')