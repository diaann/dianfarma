from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dianfarma.report_produk_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, produk):
        sheet = workbook.add_worksheet('Daftar Produk')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Produk', bold)
        sheet.write(1, 1, 'Kategori', bold)
        sheet.write(1, 2, 'Jenis Obat', bold)
        sheet.write(1, 3, 'Golongan Obat', bold)
        sheet.write(1, 4, 'Harga', bold)
        sheet.write(1, 5, 'Produsen', bold)
        row = 2
        col = 0
        for obj in produk:
            col = 0
            sheet.write(row, col, obj.name)
            for kategori in obj.kategoriproduk_id:
                sheet.write(row, col+1, kategori.name)
            for jenis in obj.jenisobat_id:
                sheet.write(row, col+2, jenis.name)
            for golongan in obj.golongan_id:
                sheet.write(row, col+3, golongan.name)
            sheet.write(row, col+4, obj.harga_jual)
            for perusahaan in obj.perusahaan_id:
                sheet.write(row, col+5, perusahaan.name)
            row += 1