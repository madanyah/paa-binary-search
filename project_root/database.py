import sqlite3
import project_root.search as search

def getConnection():
    return sqlite3.connect("dataBarang.db")
    
def buatTableBarang():
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS barang (
            nama TEXT PRIMARY KEY,
            stok INTEGER NOT NULL,
            harga INTEGER NOT NULL
        )
    """)
    con.commit()      
    cursor.close()
    con.close() 
    
def tampilkanDataBarang():
    con = getConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM barang')
    rows = cursor.fetchall()
    print("Isi tabel barang:")
    for row in rows:
        print(row)  
          
    cursor.close()
    con.close() 

def insertDataBarang(nama, stok, harga):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute("INSERT INTO barang (nama, stok, harga) VALUES (?, ?, ?)", (nama, stok, harga))
    con.commit()      
    cursor.close()
    con.close()   
    
def editDataBarang(nama, stok, harga):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute('UPDATE barang SET stok = ?, harga = ? WHERE nama = ?', (stok, harga, nama))
    con.commit()      
    cursor.close()
    con.close()   
    
def hapusDataBarang(nama):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute('DELETE FROM barang WHERE nama = ?', (nama,))       
    con.commit() 
    cursor.close()
    con.close()  

def cariBarang(namaBarang):
    conn = sqlite3.connect("dataBarang.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nama FROM barang")
    hasil = [row[0] for row in cursor.fetchall()]
    hasil.sort()

    idx = search.BinarySearch(hasil, namaBarang)
    
    if idx != -1:
        print(f"Barang ditemukan: {hasil[idx]}")
        cursor.execute('SELECT nama, stok, harga FROM barang WHERE nama = ?', (hasil[idx],))
        row = cursor.fetchone() #Pelajari lebih dalam hal ini
        print("Detail Barang:")
        print(f"Nama  : {row[0]}")
        print(f"Stok  : {row[1]}")
        print(f"Harga : {row[2]}")
    else:
        print("Barang tidak ditemukan.")
    
    cursor.close()
    conn.close()
