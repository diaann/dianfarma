from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dianfarma.report_perusahaan_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, perusahaan):
        sheet = workbook.add_worksheet('Daftar Perusahaan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'Nama Perusahaan', bold)
        sheet.write(1, 1, 'Alamat Perusahaan', bold)
        sheet.write(1, 2, 'No. Telepon', bold)
        sheet.write(1, 3, 'Produk', bold)
        row = 2
        col = 0
        for obj in perusahaan:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.no_telp)
            for produk in obj.produk_ids:
                sheet.write(row, col+3, produk.name)
                col += 1
            row += 1