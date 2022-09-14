from odoo import api, fields, models


class KategoriProduk(models.Model):
    _name = 'dianfarma.kategoriproduk'
    _description = 'New Description'

    name = fields.Selection([
        ('Obat Batuk Berdahak', 'Obat Batuk Berdahak'),
        ('Obat Flu', 'Obat Flu'),
        ('Obat Asma', 'Obat Asma'),
        ('Obat Maag', 'Obat Maag'),
        ('Obat Diare', 'Obat Diare'),
        ('Vitamin A', 'Vitamin A'),
        ('Vitamin B', 'Vitamin B'),
        ('Vitamin C', 'Vitamin C'),
        ('Vitamin D', 'Vitamin D'),
        ('Vitamin E', 'Vitamin E')
    ], string='Kategori Produk')

    kode_kategori = fields.Char(string='Kode Kategori')
    
    @api.onchange('name')
    def _compute_kode_kategori(self):
        if self.name == 'Obat Batuk Berdahak':
            self.kode_kategori = 'OB01'
        elif self.name == 'Obat Flu':
            self.kode_kategori = 'OB02'
        elif self.name == 'Obat Asma':
            self.kode_kategori = 'OB03'
        elif self.name == 'Obat Maag':
            self.kode_kategori = 'SOB04'
        elif self.name == 'Obat Diare':
            self.kode_kategori = 'OB05'
        elif self.name == 'Vitamin A':
            self.kode_kategori = 'VIT01'
        elif self.name == 'Vitamin B':
            self.kode_kategori = 'VIT02'
        elif self.name == 'Vitamin C':
            self.kode_kategori = 'VIT03'
        elif self.name == 'Vitamin D':
            self.kode_kategori = 'VIT04'
        elif self.name == 'Vitamin E':
            self.kode_kategori = 'VIT05'

    produk_ids  = fields.One2many(
        comodel_name='dianfarma.produk',
        inverse_name='kategoriproduk_id',
        string='Daftar Produk')
    
    jml_produk = fields.Char(compute='_compute_jml_produk', string='Jumlah Produk')
    
    @api.depends('produk_ids')
    def _compute_jml_produk(self):
        for record in self:
            a = self.env['dianfarma.produk'].search([('kategoriproduk_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_produk = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar Produk')
