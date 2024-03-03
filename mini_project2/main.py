from prettytable import PrettyTable

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Barang:
    def __init__(self, kode_barang, nama_barang, kondisi, harga_beli):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.kondisi = kondisi
        self.harga_beli = harga_beli

class Inventaris:
    def __init__(self):
        self.head = None

    # Create Barang awal
    def tambah_barang_awal(self, kode_barang, nama_barang, kondisi, harga_beli):
        new_barang = Barang(kode_barang, nama_barang, kondisi, harga_beli)
        new_node = Node(new_barang)

        new_node.next = self.head
        self.head = new_node

    #Create Barang akhir
    def tambah_barang_akhir(self, kode_barang, nama_barang, kondisi, harga_beli):
        new_barang = Barang(kode_barang, nama_barang, kondisi, harga_beli)
        new_node = Node(new_barang)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    #Create barang diantara
    def tambah_barang_diantara(self, kode_barang, nama_barang, kondisi, harga_beli, after_kode_barang):
        new_barang = Barang(kode_barang, nama_barang, kondisi, harga_beli)
        new_node = Node(new_barang)

        current = self.head
        prev = None
        while current is not None and current.data.kode_barang != after_kode_barang:
            prev = current
            current = current.next

        if current is not None:
            if prev is None:
                self.head = new_node
            else:
                prev.next = new_node
            new_node.next = current

    # Delete Barang awal
    def hapus_barang_awal(self):
        if self.head is not None:
            self.head = self.head.next

    #delete barang akhir
    def hapus_barang_akhir(self):
        if self.head is None:
            return

        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next

        if prev is None:
            self.head = None
        else:
            prev.next = None

    #delete barang diantara
    def hapus_barang_diantara(self, kode_barang_awal):
        current = self.head
        prev = None

        while current is not None and current.data.kode_barang != kode_barang_awal:
            prev = current
            current = current.next

        if current is not None and current.next is not None:
            node_to_delete = current.next  
            current.next = node_to_delete.next
            del node_to_delete 

        else:
            print(f"Tidak ada barang setelah barang dengan kode {kode_barang_awal} atau barang dengan kode {kode_barang_awal} tidak ditemukan")

    # Update Barang
    def update_barang(self, kode_barang, **invt):
        current = self.head
        while current is not None and current.data.kode_barang != kode_barang:
            current = current.next

        if current is not None:
            for key, value in invt.items():
                if hasattr(current.data, key):
                    setattr(current.data, key, value)
                else:
                    print(f"{key} tidak ditemukan pada barang dengan kode {kode_barang}")

    # Read Barang
    def tampilkan_data(self):
        pt = PrettyTable(["Kode Barang", "Nama Barang", "Kondisi", "Harga Beli"])
        current = inventaris.head
        while current is not None:
            pt.add_row([current.data.kode_barang, current.data.nama_barang, current.data.kondisi, current.data.harga_beli])
            current = current.next
        print(pt)

def tambah_barang():
    current = inventaris.head
    kode_barang = input("Masukkan kode barang: ")
    while current is not None:
        if current.data.kode_barang == kode_barang:
            print("Kode barang sudah ada!")
            return
        current = current.next
    nama_barang = input("Masukkan nama barang: ")
    kondisi = input("Masukkan kondisi barang: ")
    while True:
        try:
            harga_beli = int(input("Masukkan harga beli barang: "))
            break
        except ValueError:
            print("Harus Beli Harus Angka!")
    posisi = input("Pilih menambahkan barang (awal, akhir, diantara): ")
    if posisi == "awal":
        inventaris.tambah_barang_awal(kode_barang, nama_barang, kondisi, harga_beli)
    elif posisi == "akhir":
        inventaris.tambah_barang_akhir(kode_barang, nama_barang, kondisi, harga_beli)
    elif posisi == "diantara":
        after_kode_barang = input("Masukkan posisi akhir kode barang: ")
        inventaris.tambah_barang_diantara(kode_barang, nama_barang, kondisi, harga_beli, after_kode_barang)
    else:
        print("Posisi Tidak Ditemukan!")

def tampilkan_data():
    inventaris.tampilkan_data()

def ubah_barang():
    kode_barang = input("Masukkan kode barang yang ingin diubah: ")
    field = input("Masukkan field yang ingin diubah (nama_barang, kondisi, harga_beli): ")

    if field == "harga_beli":
        while True:
            try:
                new_value = int(input("Masukkan nilai baru: "))
                break
            except ValueError:
                print("Harus angka!")
    else:
        new_value = input("Masukkan nilai baru: ")

    inventaris.update_barang(kode_barang, **{field: new_value})

def hapus_barang():
    posisi = input("Masukkan posisi (awal, akhir, diantara): ")
    if posisi == "awal":
        inventaris.hapus_barang_awal()
    elif posisi == "akhir":
        inventaris.hapus_barang_akhir()
    elif posisi == "diantara":
        kode_barang_awal = input("Masukkan kode barang awal: ") 
        inventaris.hapus_barang_diantara(kode_barang_awal)
    else:
        print("Posisi Tidak Ditemukan!")

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
            exit()
        else:
            print("Maaf, pilihan  tidak ada.")

inventaris = Inventaris()

menu_utama()