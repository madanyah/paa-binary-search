class Barang: 
    def __init__(self, nama, stok, harga):
        self.nama = nama
        self.stok = stok
        self.harga = harga
    
    def pengecekan_stok(self):
        if self.stok < 0:
            raise ValueError('Stok tidak boleh minus')
    
    def pengecekan_harga(self):
        '''Belajar tentang raise dan error handling nanti'''
        if self.harga <= 0:
            raise ValueError('Harga tidak boleh minus atau nol')
        
    '''Validasi data barang masuk gaboleh sama, kecuali untuk update'''
    