from odoo import api, fields, models


class Jabatan(models.Model):
    _name = 'dianfarma.jabatan'
    _description = 'New Description'

    name = fields.Selection([
        ('Admin', 'Admin'),
        ('Kasir', 'Kasir'),
        ('Karyawan', 'Karyawan')
    ], string='Jabatan')

    kode_jabatan = fields.Char(string='Kode Jabatan')
    
    @api.onchange('name')
    def _compute_kode_jabatan(self):
        if self.name == 'Admin':
            self.kode_jabatan = 'JAB01'
        elif self.name == 'Kasir':
            self.kode_jabatan = 'JAB02'
        elif self.name == 'Karyawan':
            self.kode_jabatan = 'JAB03'

    karyawan_ids  = fields.One2many(
        comodel_name='dianfarma.karyawan',
        inverse_name='jabatan_id',
        string='Daftar Karyawan')
    
    jml_karyawan = fields.Char(compute='_compute_jml_karyawan', string='Jumlah Karyawan')
    
    @api.depends('karyawan_ids')
    def _compute_jml_karyawan(self):
        for record in self:
            a = self.env['dianfarma.karyawan'].search([('jabatan_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_karyawan = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar Karyawan')
