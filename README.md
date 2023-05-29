Soal skenario_01
Langkah :
1. Masuk ke directory dimana file python diletakkan
2. Run program dengan syntax "python skenario1.py"
3. Pilih menu yang ingin dijalankan

Soal skenario_02
Langkah :
1. Masuk ke directory dimana file python diletakkan
2. Pastikan Flask telah terinstall, jika belum jalankan "pip install Flask" di terminal atau di command prompt anda
3. Run program dengan syntax "python skenario2.py"
4. Lalu terminal akan menampilkan URL untuk kita akses, contoh "http://127.0.0.1:5000/"
5. Uji fungsi endpoint, disini saya menggunakan Postman
  - Fungsi pertama yaitu untuk membuat tugas baru dengan metode 'POST', syntax "http://127.0.0.1:5000/baru"
![Capture](https://github.com/46-45/digireg-be/assets/90466465/c1116844-f112-4efd-b141-b4186e42c267)
  - Fungsi kedua yaitu untuk mengambil daftar semua tugas dengan metode 'GET', syntax "http://127.0.0.1:5000/daftar"
![image](https://github.com/46-45/digireg-be/assets/90466465/620998eb-8245-4981-ba4f-4e1e02987786)
  - Fungsi ketiga yaitu untuk mengambil detail tugas berdasarkan ID dengan metode 'GET', syntax "http://127.0.0.1:5000/detail/{id}"
![image](https://github.com/46-45/digireg-be/assets/90466465/8e58c01b-1923-4403-bce4-730380d29c96)
  - Fungsi keempat yaitu untuk mengubah tugas berdasarkan ID dengan metode 'PUT', syntax "http://127.0.0.1:5000/ubah/{id}"
![image](https://github.com/46-45/digireg-be/assets/90466465/a68b221f-4e37-4d73-914a-016aafe8d384)
  - Fungsi kelima yaitu untuk menghapus tugas berdasarkan ID dengan metode 'DELETE', syntax "http://127.0.0.1:5000/hapus/{id}"
![image](https://github.com/46-45/digireg-be/assets/90466465/21bb3164-b5ad-4923-a4db-9267f9e1e3e0)

Soal skenario_03
Langkah :
1. Masuk ke directory dimana file python diletakkan
2. Pastikan file CSV sudah berada di directory yang sama agar memudahkan proses run
3. Run program dengan syntax "python skenario3.py"
4. Program akan mengeluarkan output pengolahan data berupa :
- penghitungan total penjualan, yaitu total semua produk yang terjual
- transaksi dengan nilai penjualan tertinggi, yaitu produk dengan jumlah terjual tertinggi
- jumlah transaksi yang dilakukan, jika ada produk yang tidak terjual maka produk tersebut tidak akan dihitung
- temukan dan cetak produk yang terjual, jika ada produk yang tidak terjual maka produk tersebut tidak akan dicetak
