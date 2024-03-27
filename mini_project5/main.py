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


    # Quick sort
    def _quick_sort(self, node, key, ascending=True):
        if node is None or node.next is None:
            return node

        pivot = node.data
        less_head = None
        less_tail = None
        equal_head = None
        equal_tail = None
        greater_head = None
        greater_tail = None

        while node is not None:
            if getattr(node.data, key) < getattr(pivot, key):
                if less_head is None:
                    less_head = less_tail = Node(node.data)
                else:
                    less_tail.next = Node(node.data)
                    less_tail = less_tail.next
            elif getattr(node.data, key) == getattr(pivot, key):
                if equal_head is None:
                    equal_head = equal_tail = Node(node.data)
                else:
                    equal_tail.next = Node(node.data)
                    equal_tail = equal_tail.next
            else:
                if greater_head is None:
                    greater_head = greater_tail = Node(node.data)
                else:
                    greater_tail.next = Node(node.data)
                    greater_tail = greater_tail.next

            node = node.next

        less_head = self._quick_sort(less_head, key, ascending=ascending)
        greater_head = self._quick_sort(greater_head, key, ascending=ascending)

        if ascending:
            sorted_list = self._concatenate_lists(less_head, equal_head, greater_head)
        else:
            sorted_list = self._concatenate_lists(greater_head, equal_head, less_head)

        return sorted_list
    
    # Quick sort nama barang
    def quick_sort_nama_barang(self, ascending=True):
        self.head = self._quick_sort(self.head, key='nama_barang', ascending=ascending)

    # Quick sort harga beli
    def quick_sort_harga_beli(self, ascending=True):
        self.head = self._quick_sort(self.head, key='harga_beli', ascending=ascending)

    # Menggabungkan 3 linked list agar jadi 1 linked list
    def _concatenate_lists(self, head1, head2, head3):
        if head1 is None:
            if head2 is None:
                return head3
            else:
                last_node = self._get_last_node(head2)
                last_node.next = head3
                return head2
        else:
            last_node = self._get_last_node(head1)
            last_node.next = head2
            last_node = self._get_last_node(head2)
            last_node.next = head3
            return head1

    # Function untuk mendapatkan node terakhir pada linked list
    def _get_last_node(self, node):
        while node is not None and node.next is not None:
            node = node.next
        return node

    # Search barang
    def cari_barang(self, key, search_by='kode_barang'):
        found_items = []
        current = self.head
        while current is not None:
            if search_by == 'kode_barang' and current.data.kode_barang == key:
                found_items.append(current.data)
            elif search_by == 'kondisi' and current.data.kondisi == key:
                found_items.append(current.data)
            current = current.next

        if found_items:
            pt = PrettyTable(["Kode Barang", "Nama Barang", "Kondisi", "Harga Beli"])
            for item in found_items:
                pt.add_row([item.kode_barang, item.nama_barang, item.kondisi, item.harga_beli])
            print("Barang ditemukan:")
            print(pt)
        else:
            print(f"Tidak ada barang dengan {search_by} '{key}' yang ditemukan.")

        return found_items
    
    # Fibonacci search
    def fibonacci_search(self, key):
        fib_m_minus_2 = 0
        fib_m_minus_1 = 1
        fib_current = fib_m_minus_1 + fib_m_minus_2

        length = self.get_length()

        while fib_current < length:
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib_current
            fib_current = fib_m_minus_1 + fib_m_minus_2

        offset = -1

        while fib_current > 1:
            i = min(offset + fib_m_minus_2, length - 1)

            if self.get_barang_at_index(i).kode_barang < key:
                fib_current = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib_current - fib_m_minus_1
                offset = i

            elif self.get_barang_at_index(i).kode_barang > key:
                fib_current = fib_m_minus_2
                fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                fib_m_minus_2 = fib_current - fib_m_minus_1

            else:
                return i

        if fib_m_minus_1 and offset < length - 1 and self.get_barang_at_index(offset + 1).kode_barang == key:
            return offset + 1

        return -1

    # memanggil barang di inventaris
    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    # Memanggil objek barang pada indeks tertentu
    def get_barang_at_index(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

# Main Fucntion
def tambah_barang():
    kode_barang = input("Masukkan kode barang: ")
    current = inventaris.head
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
            print("Harga beli harus angka!")
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
    
def sorting():
    print("Pilih Sorting")
    print("1. Urutkan Nama Barang (A-Z)")
    print("2. Urutkan Nama Barang (Z-A)")
    print("3. Urutkan Harga Beli (Murah-Mahal)")
    print("4. Urutkan Harga Beli (Mahal-Murah)")

    pilih = int(input("Masukkan pilihan: "))
    if  pilih == 1:
        inventaris.quick_sort_nama_barang(ascending=True)
    elif pilih == 2:
        inventaris.quick_sort_nama_barang(ascending=False)
    elif pilih == 3:
        inventaris.quick_sort_harga_beli(ascending=True)
    elif pilih == 4:
        inventaris.quick_sort_harga_beli(ascending=False)
    else:
        print("Pilihan tidak ditemukan.")

def fibonacci_search():
    print("Pilih kategori pencarian:")
    print("1. Berdasarkan Kode Barang")
    print("2. Berdasarkan Kondisi")

    while True:
        try:
            search_choice = int(input("Masukkan pilihan: "))

            if search_choice == 1:
                search_by = 'kode_barang'
                break
            elif search_choice == 2:
                search_by = 'kondisi'
                break
            else:
                print("Pilihan tidak valid.")
                return
        except ValueError:
            print("Input harus angka!")

    key = input("Masukkan nilai yang ingin dicari: ")

    found_items = inventaris.cari_barang(key, search_by)

def menu_utama():
    while True:
        print("Menu Utama:")
        tampilkan_data()
        print("1. Tambah Barang")
        print("2. Ubah Barang")
        print("3. Sorting")
        print("4. Hapus Barang")
        print("5. Fibonacci Search")
        print("6. Keluar")
        while True:
            try:
                pilihan = int(input("Masukkan pilihan: "))

                if pilihan == 1:
                    tambah_barang()
                    break
                elif pilihan == 2:
                    ubah_barang()
                    break
                elif pilihan == 3:
                    sorting()
                    break
                elif pilihan == 4:
                    hapus_barang()
                    break
                elif pilihan == 5:
                    fibonacci_search()
                    break
                elif pilihan == 6:
                    exit()
                else:
                    print("Maaf, pilihan tidak ada.")
            except ValueError:
                print("Harus Angka!")

inventaris = Inventaris()

inventaris.tambah_barang_awal("VisO123", "Kursi", "Baik", 5000)
inventaris.tambah_barang_awal("VsO13", "Meja", "Rusak", 50000)
inventaris.tambah_barang_awal("LiTO13", "Monitor", "Baik", 705000)
inventaris.tambah_barang_awal("OisO23", "Lapto", "Rusak", 25000)
inventaris.tambah_barang_awal("KVsO13", "Laptop", "Baik", 605000)

menu_utama()