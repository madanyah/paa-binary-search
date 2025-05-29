import src.database as database
from src.barang import Barang
import src.search as search

def main():
    database.buatTableBarang()
    
    while True:
        print(' ')
        print('=' * 5, ' Program Manajemen Barang ', '='* 5)
        print('1. Tampilkan Data Barang')
        print('2. Tambahkan Barang')
        print('3. Edit Barang')
        print('4. Hapus Barang')
        print('5. Cari Barang')
        pil = int(input('Masukkan Pilihanmu = '))

        match pil:
            case 1:
                database.tampilkanDataBarang()

            case 2:
                nama = input('Masukkan Nama Barang = ')
                stok = int(input('Masukkan Jumlah Stok = '))
                harga = int(input('Masukkan Harga Satuan = '))
                
                newBarang = Barang(nama, stok, harga)

                try:
                    newBarang.pengecekan_stok()
                    newBarang.pengecekan_harga()
                    database.insertDataBarang(newBarang.nama, newBarang.stok, newBarang.harga)
                    print("Barang berhasil ditambahkan!")

                except ValueError as e:
                    print(f"Error saat menambahkan barang: {e}")

            case 3:
                nama = input('Masukkan Nama Barang = ')
                stok = input('Masukkan Stok Baru = ')
                harga = input('Masukkan Harga = ')
                
                database.editDataBarang(nama, stok, harga)
            case 4:
                nama = input("Masukkan nama barang yang ingin dihapus: ")
                database.hapusDataBarang(nama)
                #Tambahkan error penghapusan barang
                print("Barang berhasil dihapus!")

            case 5:
                nama = input('Masukkan Nama Barang yang Dicari = ')
                database.cariBarang(nama)
                
            case _:
                print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
