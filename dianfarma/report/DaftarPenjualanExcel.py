from odoo import models, fields


class PartnerXlsx(models.AbstractModel):
    _name = 'report.dianfarma.report_transaksi_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, transaksi):
        sheet = workbook.add_worksheet('Daftar Transaksi')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'No. Nota', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tanggal Transaksi', bold)
        sheet.write(1, 3, 'Total Pembayaran', bold)
        sheet.write(1, 4, 'Daftar Barang', bold)
        row = 2
        col = 0
        for obj in transaksi:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.nama_pelanggan)
            sheet.write(row, col+2, str(obj.tgl_transaksi))
            sheet.write(row, col+3, obj.total)
            for produk in obj.detailtransaksi_ids.produk_id:
                sheet.write(row, col+4, produk.name)
                col += 1
            row += 1