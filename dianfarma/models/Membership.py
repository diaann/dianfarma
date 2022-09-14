from odoo import api, fields, models


class Membership(models.Model):
    _name = 'dianfarma.membership'
    _description = 'New Description'

    name = fields.Char(
        string='Nama',
        required=True)
    alamat = fields.Char(string='Alamat')
    jenis_kelamin = fields.Selection([
        ('Laki-laki', 'Laki-laki'),
        ('Perempuan', 'Perempuan'),
    ], string='Jenis Kelamin')
    no_tlp = fields.Char(string='No. Telepon')
    tgl_daftar = fields.Datetime(
        string='Tanggal Pendaftaran',
        default=fields.Datetime.now())
    masa_berlaku = fields.Char(string='Masa Berlaku')
