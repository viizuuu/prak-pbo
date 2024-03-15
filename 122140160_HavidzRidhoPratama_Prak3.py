class Dagangan:
    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        self.jumlah_barang = 0
        self.list_barang = []

    def tambah_barang(self, nama_barang, stok_barang, harga_barang):
        self.list_barang.append({"nama": nama_barang, "stok": stok_barang, "harga": harga_barang})
        self.jumlah_barang += 1

    def lihat_barang(self):
        print(f"Jumlah barang dagangan pada toko : {self.jumlah_barang} buah")
        for barang in self.list_barang:
            print(f"{barang['nama']}, Seharga Rp.{barang['harga']}, (Stok : {barang['stok']})")

    def hapus_barang(self, nama_barang):
        for barang in self.list_barang:
            if barang['nama'] == nama_barang:
                self.list_barang.remove(barang)
                self.jumlah_barang -= 1
                print(f"{nama_barang} telah dihapus dari toko.")
    
Dagangan1 = Dagangan("Galon Aqua 19l", 32, 17000)
Dagangan1.tambah_barang("Gas LPG 5kg", 22, 88000)
Dagangan1.tambah_barang("Beras Ramos 5kg", 13, 68000)

Dagangan1.lihat_barang()
Dagangan1.hapus_barang("Galon Aqua 19l")
Dagangan1.lihat_barang()
Dagangan1.hapus_barang("Gas LPG 5kg")
Dagangan1.hapus_barang("Beras Ramos 5kg")

