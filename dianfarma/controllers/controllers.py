from odoo import http, models, fields
from odoo.http import request, Response
import json


class Dianfarma(http.Controller):
    # GET KATEGORI PRODUK
    @http.route('/dianfarma/getkategoriproduk', auth='public', method=['GET'])
    def getKategoriProduk(self, **kw):
        kategoriproduk = request.env['dianfarma.kategoriproduk'].search([])
        isi = []
        for bb in kategoriproduk:
            all_produk = []
            for prod in bb.produk_ids:
                produk = prod.name
                all_produk.append(produk)

            isi.append({
                'kategori_produk' : bb.name,
                'kode_kategori' : bb.kode_kategori,
                'jumlah_produk' : bb.jml_produk,
                'produk' : all_produk
            })
        return Response(json.dumps(isi), content_type='application/json')
    

    # GET JENIS OBAT
    @http.route('/dianfarma/getjenisobat', auth='public', method=['GET'])
    def getJenisObat(self, **kw):
        jenisobat = request.env['dianfarma.jenisobat'].search([])
        isi = []
        for bb in jenisobat:
            all_produk = []
            for prod in bb.produk_ids:
                produk = prod.name
                all_produk.append(produk)

            isi.append({
                'jenis_obat' : bb.name,
                'kode_obat' : bb.kode_obat,
                'jumlah_produk' : bb.jml_produk,
                'produk' : all_produk
            })
        return Response(json.dumps(isi), content_type='application/json')
    

    # GET GOLONGAN OBAT
    @http.route('/dianfarma/getgolonganobat', auth='public', method=['GET'])
    def getGolonganObat(self, **kw):
        golonganobat = request.env['dianfarma.golonganobat'].search([])
        isi = []
        for bb in golonganobat:
            all_produk = []
            for prod in bb.produk_ids:
                produk = prod.name
                all_produk.append(produk)

            isi.append({
                'golongan_obat' : bb.name,
                'kode_golongan_obat' : bb.kode_golongan,
                'jumlah_produk' : bb.jml_produk,
                'produk' : all_produk
            })
        return Response(json.dumps(isi), content_type='application/json')
    

    # GET PRODUK
    @http.route('/dianfarma/getproduk', auth='public', method=['GET'])
    def getProduk(self, **kw):
        produk = request.env['dianfarma.produk'].search([])
        isi = []
        for bb in produk:
            isi.append({
                'nama_produk' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return Response(json.dumps(isi), content_type='application/json')
    

    # GET JABATAN
    @http.route('/dianfarma/getjabatan', auth='public', method=['GET'])
    def getJabatan(self, **kw):
        jabatan = request.env['dianfarma.jabatan'].search([])
        isi = []
        for bb in jabatan:
            all_karyawan = []
            for jml in bb.karyawan_ids:
                karyawan = jml.name
                all_karyawan.append(karyawan)

            isi.append({
                'jabatan' : bb.name,
                'kode_jabatan' : bb.kode_jabatan,
                'jumlah_karyawan' : bb.jml_karyawan,
                'karyawan' : all_karyawan
            })
        return Response(json.dumps(isi), content_type='application/json')
    

    # GET KARYAWAN
    @http.route('/dianfarma/getkaryawan', auth='public', method=['GET'])
    def getKaryawan(self, **kw):
        karyawan = request.env['dianfarma.karyawan'].search([])
        pegawai = []
        for kar in karyawan:
            for k in kar.jabatan_id:
                jabatan = k.name

            pegawai.append({
                'nama_karyawan' : kar.name,
                'jenis_kelamin' : kar.jenis_kelamin,
                'no_telepon' : kar.no_tlp,
                'jabatan': jabatan
            })
                
        return Response(json.dumps(pegawai), content_type='application/json')
    

    # GET PERUSAHAAN
    @http.route('/dianfarma/getperusahaan', auth='public', method=['GET'])
    def getPerusahaan(self, **kw):
        perusahaan = request.env['dianfarma.perusahaan'].search([])
        sup = []
        for pr in perusahaan:
            nama_perusahaan = pr.name
            alamat = pr.alamat
            no_telp = pr.no_telp

            produk = []
            for p in pr.produk_ids:
                all_produk = p.name
                produk.append(all_produk)
            
            sup.append({
                'perusahaan' : nama_perusahaan,
                'alamat' : alamat,
                'no_telepon' : no_telp,
                'produk': produk
            })
                
        return Response(json.dumps(sup), content_type='application/json')
    
    # GET MEMBERSHIP
    @http.route('/dianfarma/getmembership', auth='public', method=['GET'])
    def getMembership(self, **kw):
        membership = request.env['dianfarma.membership'].search([])
        member = []
        for m in membership:
            member.append({
                'nama' : m.name,
                'alamat' : m.alamat,
                'jenis_kelamin' : m.jenis_kelamin,
                'no_telepon' : m.no_tlp,
                'tgl_daftar': str(m.tgl_daftar),
                'masa_berlaku': m.masa_berlaku
            })
                
        return Response(json.dumps(member), content_type='application/json')
    
    
    # GET TRANSAKSI
    @http.route('/dianfarma/gettransaksi', auth='public', method=['GET'])
    def getTransaksi(self, **kw):
        transaksi = request.env['dianfarma.transaksi'].search([])
        isi = []
        for rec in transaksi:
            produk = []
            for p in rec.detailtransaksi_ids:
                all_qty = p.qty
                all_produk = p.produk_id.name
                produk.append({
                    'nama_produk' : all_produk,
                    'quantity' : all_qty
                })
            
            isi.append({
                'no_nota' : rec.name,
                'nama_pelanggan' : rec.nama_pelanggan,
                'tgl_transaksi' : str(rec.tgl_transaksi),
                'total' : rec.total,
                'produk': produk
            })
                
        return Response(json.dumps(isi), content_type='application/json')