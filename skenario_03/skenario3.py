import csv

# Fungsi untuk membaca file CSV dan mengembalikan data
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Fungsi untuk menghitung total penjualan
def calculate_total_sales(data):
    total_sales = 0
    for row in data:
        total_sales += int(row['jumlah'])
    return total_sales

# Fungsi untuk mencari transaksi dengan penjualan tertinggi
def find_highest_sales_transaction(data):
    max_sales = 0
    transaction = None
    for row in data:
        sales = int(row['jumlah'])
        if sales > max_sales:
            max_sales = sales
            transaction = row
    return transaction

# Fungsi untuk menghitung jumlah transaksi
def calculate_transaction_count(data):
    count = 0
    for row in data:
        if int(row['jumlah']) != 0:
            count += 1
    return count

# Fungsi untuk mencetak daftar produk yang terjual
def print_sold_products(data):
    sold_products = []
    for row in data:
        if int(row['jumlah']) != 0:
            sold_products.append(row['produk'])
    print(", ".join(sold_products))

# Path file CSV
file_path = 'data.csv'

# Membaca file CSV
data = read_csv_file(file_path)

# Menghitung total penjualan
total_sales = calculate_total_sales(data)
print("Total penjualan: ", total_sales)

# Mencari transaksi dengan penjualan tertinggi
highest_sales_transaction = find_highest_sales_transaction(data)
if highest_sales_transaction:
    print(f"Transaksi dengan penjualan tertinggi: {highest_sales_transaction['produk']}")
else:
    print("Tidak ada transaksi yang ditemukan.")

# Menghitung jumlah transaksi
transaction_count = calculate_transaction_count(data)
print("Jumlah transaksi:", transaction_count)

# Mencetak daftar produk yang terjual
print("Daftar produk yang terjual:", end=" ")
print_sold_products(data)
