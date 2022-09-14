from odoo import api, fields, models


class JenisObat(models.Model):
    _name = 'dianfarma.jenisobat'
    _description = 'New Description'

    name = fields.Selection([
        ('Tablet', 'Tablet'),
        ('Pil', 'Pil'),
        ('Kapsul', 'Kapsul'),
        ('Sirup', 'Sirup'),
        ('Serbuk', 'Serbuk'),
        ('Salep', 'Salep'),
        ('Obat Tetes', 'Obat Tetes')
    ], string='Jenis Obat')

    kode_obat = fields.Char(string='Kode Jenis Obat')
    
    @api.onchange('name')
    def _compute_kode_obat(self):
        if self.name == 'Tablet':
            self.kode_obat = 'JO01'
        elif self.name == 'Pil':
            self.kode_obat = 'JO02'
        elif self.name == 'Kapsul':
            self.kode_obat = 'JO03'
        elif self.name == 'Sirup':
            self.kode_obat = 'JO04'
        elif self.name == 'Serbuk':
            self.kode_obat = 'JO05'
        elif self.name == 'Salep':
            self.kode_obat = 'JO06'
        elif self.name == 'Obat Tetes':
            self.kode_obat = 'JO07'
    
    produk_ids  = fields.One2many(
        comodel_name='dianfarma.produk',
        inverse_name='jenisobat_id',
        string='Daftar Produk')
    
    jml_produk = fields.Char(compute='_compute_jml_produk', string='Jumlah Produk')
    
    @api.depends('produk_ids')
    def _compute_jml_produk(self):
        for record in self:
            a = self.env['dianfarma.produk'].search([('jenisobat_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_produk = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar Produk')
