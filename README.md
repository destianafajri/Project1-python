# Project1-python
## Latar Belakang
Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya dengan harapan 
1. Customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
2. Customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. 

## Requirements
1. Customer membuat ID transaksi customer dengan membuat objek dari function : trnsct_123 = transaction().
2. Kemudian, Customer memasukkan nama item, jumlah item, dan harga barang yang ingin dibeli
	add_item([<nama item>, <jumlah item>, <harga per item>])
3.Jika ternyata ada kesalahan dalam memasukkan nama item atau jumlah item atau harga item tetapi tidak ingin menghapus itemnya, Customer bisa melakukan
  1.Update nama item dengan method: 
  update_item_name(<nama item>, <update nama item>)
  2.Update jumlah item dengan method: 
  update_item_qty(<nama_item>, <update jumlah item>)
  3.Update harga item menggunakan method: 
  update_item_price(<nama_item>, <update harga item>)
4. Jika batal membeli item belanjaan, Customer bisa melakukan
   1.Menghapus salah satu item dari nama item dengan method : 
    delete_item(<nama item>)
    Ketika menghapus salah satu nama item, maka jumlah item dan harga per item pada baris/list tersebut akan ikut terhapus
   2.Langsung menghapus semua transaksi atau reset transaksi dengan method :
     reset_transaction()
5. Customer sudah selesai dengan berbelanja online nya, tetapi Customer masih ragu apakah harga barang dan nama barang yang diinput sudah benar. Bisa saja Customer melakukan kesalahan dalam melakukan input, semisal sudah melakukan input harga barang tetapi lupa untuk input nama barangnya. Andi bisa menggunakan method check_order(). Terdapat ketentuan:
    1.Akan mengeluarkan pesan “Pemesanan sudah benar” (bebas bisa dengan message yang lain) jika tidak ada kesalahan input 
      Akan mengeluarkan pesan “Terdapat kesalahan input data” jika terjadi kesalahan input
    2.Keluarkan output transaksi atau pemesanan apa saja yang sudah dibeli.
6. Setelah melakukan pengecekan, Customer bisa menghitung total belanja yang sudah dibeli. Andi bisa menggunakan method check_out(). Pada supermarket ini ternyata terdapat     ketentuan:
    Jika total harga per item Andi diatas Rp 200.000 maka akan mendapatkan diskon 5%
    Jika total harga per item Andi diatas Rp 300.000 maka akan mendapatkan diskon 6%
    Jika total harga per item Andi diatas Rp 500.000 maka akan mendapatkan diskon 7%
    Total pembelian hanya ditampilkan pada method check_out(), namun tidak di simpan di dalam database

7. Setiap kali method check_out() dijalankan, data transaksi dimasukkan ke dalam sqlite database pada tabel transaction menggunakan fungsi insert_to_table(<source_data>) 
    Kolom yang disimpan pada database
    1.no_id : nomer id (auto increment)
    2.nama_item : nama barang yang dibeli
    3.jumlah_item : jumlah barang yang dibeli
    4.harga : harga barang 
    5.total_harga : total harga (jumlah item * harga)
    6.diskon : potongan harga
    7.harga_diskon : harga item setelah diskon
 


  




