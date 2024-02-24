from prettytable import PrettyTable

class Barang:
    _kode_terakhir = 0

    def __init__(self, nama_barang, kondisi, harga_beli):
        Barang._kode_terakhir += 1
        self.kode_barang = f"BRG{Barang._kode_terakhir:03d}"
        self.nama_barang = nama_barang
        self.kondisi = kondisi
        self.harga_beli = harga_beli

    

class Inventaris:
    def __init__(self):
        self.daftar_barang = []

    # Create Barang
    def tambah_barang(self, nama_barang, kondisi, harga_beli):
        barang = Barang(nama_barang, kondisi, harga_beli)
        inventaris.daftar_barang.append(barang)

        for i, barang in enumerate(inventaris.daftar_barang, start=1):
            barang.kode_barang = f"BRG{i:03d}"
    
    # Delete Barang
    def hapus_barang(self, kode_barang):
        for barang in self.daftar_barang:
            if barang.kode_barang == kode_barang:
                self.daftar_barang.remove(barang)
                break
            else:
                print("Data Tidak Valid")

        for i, barang in enumerate(self.daftar_barang, start=1):
            barang.kode_barang = f"BRG{i:03d}"

    # Update Barang
    def update_barang(self, kode_barang, **invt):
        for barang in self.daftar_barang:
            if barang.kode_barang == kode_barang:
                for key, value in invt.items():
                    if hasattr(barang, key):
                        setattr(barang, key, value)
                    else:
                        print(f"Field {key} tidak ditemukan pada barang dengan kode {kode_barang}")
                break
            else:
                print("Data Tidak Ditemukan!")

    # Read Barang
    def tampilkan_data(self):
        table = PrettyTable()
        table.field_names = ["Kode Barang", "Nama Barang", "Kondisi", "Harga Beli"]
        for barang in self.daftar_barang:
            table.add_row([
                barang.kode_barang,
                barang.nama_barang,
                barang.kondisi,
                barang.harga_beli
            ])
        print(table)

def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    kondisi = input("Masukkan kondisi barang: ")
    while True:
        try:
            harga_beli = int(input("Masukkan harga beli barang: "))
            break
        except ValueError:
            print("Harus Angka!")

    inventaris.tambah_barang(nama_barang, kondisi, harga_beli)

def tampilkan_data():
    inventaris.tampilkan_data()

def ubah_barang():
    kode_barang = input("Masukkan kode barang yang ingin diubah: ")
    field = input("Masukkan field yang ingin diubah (nama_barang, kondisi, harga_beli): ")
    new_value = input("Masukkan nilai baru: ")

    inventaris.update_barang(kode_barang, **{field: new_value})

def hapus_barang():
    kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
    inventaris.hapus_barang(kode_barang)

def menu_utama():
    while True:
        tampilkan_data()
        print("1. Tambah Barang")
        print("2. Ubah Barang")
        print("3. Hapus Barang")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            ubah_barang()
        elif pilihan == "3":
            hapus_barang()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")


inventaris = Inventaris()


menu_utama()