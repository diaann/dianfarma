from odoo import api, fields, models


class Golongan(models.Model):
    _name = 'dianfarma.golonganobat'
    _description = 'New Description'

    name = fields.Selection([
        ('Obat Bebas', 'Obat Bebas'),
        ('Obat Bebas Terbatas', 'Obat Bebas Terbatas'),
        ('Obat Keras', 'Obat Keras'),
        ('Obat Golongan Narkotika', 'Obat Golongan Narkotika'),
        ('Obat Fitofarmaka', 'Obat Fitofarmaka'),
        ('Obat Herbal Terstandar (OHT)', 'Obat Herbal Terstandar (OHT)'),
        ('Obat Herbal (Jamu)', 'Obat Herbal (Jamu)')
    ], string='Golongan Obat')

    kode_golongan = fields.Char(string='Kode Golongan')
    
    @api.onchange('name')
    def _compute_kode_golongan(self):
        if self.name == 'Obat Bebas':
            self.kode_golongan = 'GOL1'
        elif self.name == 'Obat Bebas Terbatas':
            self.kode_golongan = 'GOL2'
        elif self.name == 'Obat Keras':
            self.kode_golongan = 'GOL3'
        elif self.name == 'Obat Golongan Narkotika':
            self.kode_golongan = 'GOL'
        elif self.name == 'Obat Fitofarmaka':
            self.kode_golongan = 'GOL5'
        elif self.name == 'Obat Herbal Terstandar (OHT)':
            self.kode_golongan = 'GOL6'
        elif self.name == 'Obat Herbal (Jamu)':
            self.kode_golongan = 'GOL7'

    image = fields.Image('Logo Golongan')
    produk_ids  = fields.One2many(
        comodel_name='dianfarma.produk',
        inverse_name='golongan_id',
        string='Daftar Produk')
    
    jml_produk = fields.Char(compute='_compute_jml_produk', string='Jumlah Produk')
    
    @api.depends('produk_ids')
    def _compute_jml_produk(self):
        for record in self:
            a = self.env['dianfarma.produk'].search([('golongan_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_produk = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar Produk')
