import transaksi


def main():

    while(True):
        menu()
        menu_inp = int(input("Masukkan Menu Pilihan Anda : "))
        if (menu_inp == 1):
            # tambah barang
            nama_item = input("Masukkan Nama Item : ")
            jumlah_item = int(input("Masukkan jumlah item : "))
            harga_per_item = int(input("Masukkan harga per item : "))
            total_harga = jumlah_item*harga_per_item
            transaksi.add_item(nama_item, jumlah_item,
                               harga_per_item, total_harga)
            print("----- Barang berhasil ditambah ke keranjang -----")
        elif (menu_inp == 2):
            # lihat keranjang
            transaksi.print_list_belanja()
            input_konfirmasi = input("Apakah lanjut check out(ya/tidak)? ")
            if (input_konfirmasi == 'ya'):
                # menampilkan total bayar

                print("Total yang harus dibayar adalah : ")

            elif(input_konfirmasi == 'tidak'):
                return main()
            else:
                print("pilihan tidak ada")
        elif (menu_inp == 3):
            # edit barang2
            print("1. Edit Nama Item")
            print("2. Edit Harga Per Item")
            print("3. Edit Jumlah Item")
            input_edit = int(input("Masukkan Menu Pilihan Anda : "))
            if (input_edit == 1):
                # edit nama item
                nama_item = input("Masukkan nama item yang ingin diubah : ")
                nama_baru = input("Masukkan nama baru item : ")
                transaksi.edit_nama_item(nama_item, nama_baru)
                print("----- Nama barang berhasil diubah -----")
            elif (input_edit == 2):
                # edit harga per item
                nama_item = input(
                    "Masukkan nama item yang harganya ingin di ubah : ")
                harga_baru = int(input("Masukkan harga baru Item : "))
                transaksi.edit_harga_item(nama_item, harga_baru)
                print("----- Harga per item berhasil diubah -----")
            elif (input_edit == 3):
                # edit jumlah item
                nama_item = input(
                    "Masukkan nama item yang jumlahnya ingin di ubah : ")
                jumlah_baru = int(input("Masukkan jumlah Item : "))
                transaksi.edit_jumlah_item(nama_item, jumlah_baru)
                print("----- Jumlah item berhasil diubah -----")
            else:
                print("Pilihan Tidak Ada")
        elif (menu_inp == 4):
            # hapus barang
            print("1. Hapus Satu Item")
            print("2. Hapus Semua Item")
            input_hapus = int(input("Masukkan Menu Pilihan Anda : "))
            if (input_hapus == 1):
                # hapus satu item
                nama_item = input("Masukkan nama item yang ingin dihapus : ")
                transaksi.delete_item(nama_item)
                print("Item %s berhasil di hapus" % nama_item)

            elif (input_hapus == 2):
                # hapus semua item
                transaksi.reset_transaction()
                print("Semua item berhasil dihapus")
        elif (menu_inp == 5):
            # Keluar program
            print("Terima Kasih")
            break

        else:
            print("Pilihan Menu Tidak Ada")


def menu():
    print("====== Destiana Beauty ======")
    print("-----------------------------")
    print("""====== Daftar Produk ======
----------------------------------------
| No | Nama Produk | Harga Produk |
----------------------------------------
| 1 | Bedak Padat | 55000  |
| 2 | Lipstik     | 25000  |
| 3 | Eyeliner    | 43000  |
| 4 | Foundation  | 145000 |
----------------------------------------
    """)
    print("1. Tambah Barang ke Keranjang")
    print("2. Lihat Keranjang")
    print("3. Edit Barang")
    print("4. Hapus Barang")
    print("5. Keluar Program")


if __name__ == "__main__":
    main()
