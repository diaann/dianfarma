from odoo import api, fields, models


class Karyawan(models.Model):
    _name = 'dianfarma.karyawan'
    _description = 'New Description'

    name = fields.Char(string='Nama Karyawan')
    jenis_kelamin = fields.Selection([
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ], string='Jenis Kelamin')
    alamat = fields.Char(string='Alamat')
    no_tlp = fields.Char(string='Nomor Telepon')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    jabatan_id = fields.Many2one(
        comodel_name='dianfarma.jabatan',
        string='Jabatan',
        ondelete='cascade')
