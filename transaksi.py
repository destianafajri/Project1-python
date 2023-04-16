
# list carts yang menyimpan nama item, jumlah item yang di beli,
# dan harga per item


list_belanja = []


def add_item(nama_item, jumlah_item, harga_per_item, total_harga):
    if type(nama_item) != str:
        return False
    if type(jumlah_item) != int:
        return False
    if type(harga_per_item) != int:
        return False
    list_belanja.append(
        [nama_item, jumlah_item, harga_per_item, total_harga])
    return True

# mengubah nama item


def edit_nama_item(nama_item, nama_baru):
    for barang in list_belanja:
        if barang[0] == nama_item:
            barang[0] = nama_baru
    return True

# mengubah jumlah item di keranjang


def edit_jumlah_item(nama_item, jumlah_baru):
    for barang in list_belanja:
        if barang[0] == nama_item:
            barang[1] = jumlah_baru
    return True

# mengubah harga per item


def edit_harga_item(nama_item, harga_baru):
    for barang in list_belanja:
        if barang[0] == nama_item:
            barang[2] = harga_baru
    return True

# delete item


def delete_item(nama_item):
    for index, barang in enumerate(list_belanja):
        if barang[0] == nama_item:
            break

    list_belanja.pop(index)
    return True

# reset transaksi


def reset_transaction():
    list_belanja.clear()
    print("Berhasil menghapus semua barang yang ada di keranjang")


# print list belanja

def print_list_belanja():
    print("======================================================")
    print("Nama Produk | Jumlah | Harga per Item | Total Harga | Diskon | Harga Setelah Diskon")
    for i in list_belanja:
        print(*i)
    print("======================================================")


# check out belanja
"""
total_pesanan = []

def cek_diskon(nama_item,jml_item,total_harga):
    print("Produk yang dibeli adalah : ")
    total_pesanan.append[nama_item,jml_item,total_harga]


def besar_diskon(diskon, nama_item, total_harga):
    for barang in list_belanja:
        if barang[0] == nama_item:
            barang[4] = diskon
            diskon = besar_diskon-total_harga
            if(total_harga >= 200000):
                besar_diskon = total_harga-(5/100)
            elif(total_harga >= 300000):
                besar_diskon = total_harga-(6/100)
            elif(total_harga >= 500000):
                besar_diskon = total_harga-(7/100)
            else:
                besar_diskon = 0
    return True


def harga_after_diskon(nama_item, diskon, total_harga, harga_baru_diskon):
    for barang in list_belanja:
        if barang[0] == nama_item:
            barang[5] = harga_baru_diskon
            harga_baru_diskon = total_harga-diskon
    return True
"""
