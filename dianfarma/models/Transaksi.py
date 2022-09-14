from odoo import api, fields, models
# from odoo.exceptions import UserError, ValidationError

class Transaksi(models.Model):
    _name = 'dianfarma.transaksi'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pelanggan = fields.Char(string='Nama Pembeli')
    tgl_transaksi = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total = fields.Integer(
        compute='_compute_total',
        string='Total Pembayaran')
    detailtransaksi_ids = fields.One2many(
        comodel_name='dianfarma.detailtransaksi', 
        inverse_name='transaksi_id', 
        string='Detail Transaksi')

    @api.depends('detailtransaksi_ids')
    def _compute_total(self):
        for rec in self:
            a = sum(self.env['dianfarma.detailtransaksi'].search(
                [('transaksi_id', '=', rec.id)]).mapped('subtotal'))
            rec.total = a

    def unlink(self):
        if self.detailtransaksi_ids:
            a=[]
            for rec in self:
                a = self.env['dianfarma.detailtransaksi'].search([('transaksi_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.produk_id.name) + ' ' + str(ob.qty))
                ob.produk_id.stok += ob.qty
        record = super(Transaksi,self).unlink()

    def write(self,vals):
        for rec in self:
            a = self.env['dianfarma.detailtransaksi'].search([('transaksi_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.produk_id.name)+' '+str(data.qty)+' '+str(data.produk_id.stok))
                data.produk_id.stok += data.qty
        record = super(Transaksi,self).write(vals)
        for rec in self:
            b = self.env['dianfarma.detailtransaksi'].search([('transaksi_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.produk_id.name)+' '+str(databaru.qty)+' '+str(databaru.produk_id.stok))
                    databaru.produk_id.stok -= databaru.qty
                else:
                    pass
        return record


class DetailTransaksi(models.Model):
    _name = 'dianfarma.detailtransaksi'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    transaksi_id = fields.Many2one(
        comodel_name='dianfarma.transaksi',
        string='Detail Transaksi')
    produk_id = fields.Many2one(
        comodel_name='dianfarma.produk',
        string='Daftar Produk')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantitiy')
    subtotal = fields.Integer(
        compute='_compute_subtotal', 
        string='Sub Total')
    
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('produk_id')
    def _onchange_produk_id(self):
        if (self.produk_id.harga_jual):
            self.harga_satuan = self.produk_id.harga_jual
    
    @api.model
    def create(self,vals):
        record = super(DetailTransaksi,self).create(vals)
        if record.qty:
            self.env['dianfarma.produk'].search(
                [('id','=',record.produk_id.id)]
                ).write({'stok': record.produk_id.stok - record.qty})
        return record
    
    # @api.constrains('qty')
    # def check_quantity(self):
    #     for rec in self:
    #         if rec.qty < 1:
    #             raise ValidationError("Tentukan quantity untuk {}".format(rec.produk_id.name))
    #         elif (rec.produk_id.stok < rec.qty):
    #             raise ValidationError("Stok untuk {} tidak mencukupi. Untuk saat ini, produk tersebut hanya tersedia sebanyak {}".format(rec.produk_id.name,rec.produk_id.stok))

