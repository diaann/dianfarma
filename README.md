## table of contents
1. [about](#about)
2. [features](#features)
3. [how to use](#how-to-use)

## about
this project was created using odoo 15. this project is expected to facilitate and assist companies, groups or individuals in collecting data or archiving data at pharmacies. 

## features
there are several features that can be used, namely:
1. menu produk
this menu is divided into 4 sections or categories, there are 'kategori produk', 'jenis obat', 'golongan obat', and 'daftar produk'. this menu can be used to store data about any products. 

**daftar produk**

![image](https://user-images.githubusercontent.com/82097499/190166637-86159516-3940-4342-b185-7bc8da22328b.png)

**kategori produk**

![image](https://user-images.githubusercontent.com/82097499/190169608-511565c1-7edc-4ec7-8f61-2adf7ade5821.png)

2. menu karyawan
this menu is divided into 2 categories, namely 'jabatan' and 'karyawan'. this menu can be used to store employee data.

**karyawan**

![image](https://user-images.githubusercontent.com/82097499/190170821-5627cc37-ca29-4436-a501-ebc5bc5b5758.png)

3. menu perusahaan
this menu can be used to store company data that produces the product.

**perusahaan**

![image](https://user-images.githubusercontent.com/82097499/190171571-559f5415-bcf9-47b8-8043-178f9ced6b90.png)

4. menu membership

**membership**

![image](https://user-images.githubusercontent.com/82097499/190172094-ac68742e-3f10-480e-a6c1-e6f29b80702d.png)

5. menu transaksi
this menu is used to store sales or transaction data.

**transaksi**

![image](https://user-images.githubusercontent.com/82097499/190172249-165578ae-c91d-4930-972a-c7eba46f3063.png)

## how to use
1. install odoo 15, python 3.8.13, and pip 22.2.2.
2. in the installed odoo folder, create a new folder with the name addonsproject, then clone the repository and save it in the addonsproject folder.
3. if you haven't created a user yet, create a postgresql user first.
```
sudo -u postgres createuser -s $USER
```
4. create a dianfarma database.
```
createdb dianfarma
```
5. create a runserver file then enter the following code in runserver file.
```
./odoo-bin --addons-path=/home/dian/odooproject/odoo/addons,/home/dian/odooproject/odoo/addonsproject --xmlrpc-port=8060 --db_port 5432 -d dianfarma --limit-memory-hard 0 --limit-time-real=10000 -u dianfarma
```
6. run the runserver file.
```
./runserver
```
7. in the browser, open localhost:8060. for username and password enter 'admin'.
