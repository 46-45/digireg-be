class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class AddressBook:
    def __init__(self):
        self.contacts = []

    #Fungsi untuk menambah kontak
    def add_contact(self, name: str, phone_number: str) -> None:
        if phone_number.isdigit():
            contact = Contact(name, phone_number)
            self.contacts.append(contact)
            print("Kontak berhasil ditambahkan")
        else:
            print("Nomor telepon tidak valid")

    #Fungsi untuk menghapus kontak
    def remove_contact(self, name: str) -> None:
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Kontak berhasil dihapus")
                break
        else:
            print("Kontak tidak ditemukan")

    #Fungsi untuk mencari kontak
    def search_contact(self, name: str) -> str:
        for contact in self.contacts:
            if contact.name == name:
                return contact.phone_number
        return "Kontak tidak ditemukan"


# Fungsi untuk menampilkan menu
def display_menu():
    print("=== Pengelolaan Buku Telepon ===")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak dengan Nama")
    print("0. Keluar")


# Membuat objek AddressBook
address_book = AddressBook()

# Loop menu
while True:
    display_menu()
    choice = input("Pilih menu : ")

    if choice == "1":
        name = input("Nama: ")
        phone_number = input("Nomor Telepon: ")
        address_book.add_contact(name, phone_number)

    elif choice == "2":
        name = input("Nama Kontak yang ingin dihapus: ")
        address_book.remove_contact(name)

    elif choice == "3":
        name = input("Nama Kontak yang ingin dicari: ")
        result = address_book.search_contact(name)
        print(result)

    elif choice == "0":
        print("Terima kasih")
        break

    else:
        print("Menu tidak valid")