from odoo import api, fields, models


class ProdukDatang(models.TransientModel):
    _name = 'dianfarma.produkdatang'
    
    produk_id = fields.Many2one(
        comodel_name='dianfarma.produk', 
        string='Nama produk',
        required=True)
    
    jumlah = fields.Integer(
        string= 'Jumlah',
        required=False)
    
    def button_produkdatang(self):
        for rec in self:
            self.env['dianfarma.produk'].search([('id', '=', rec.produk_id.id)]).write({'stok': rec.produk_id.stok + rec.jumlah})
