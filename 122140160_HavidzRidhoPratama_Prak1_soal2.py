pi = 3.14 

def hitung_luas_dan_keliling_lingkaran(jari_jari):
    if jari_jari < 0:
        print("Jari-jari lingkaran tidak boleh negatif")
        return
    
    # Menghitung luas lingkaran
    luas = pi * jari_jari ** 2
    
    # Menghitung keliling lingkaran
    keliling = 2 * pi * jari_jari
    
    # Mencetak hasil
    print("luas : ", luas)
    print("keliling : ", keliling)

# Menerima input dari pengguna dan menangani kesalahan input
try:
    jari_jari = float(input("jari-jari : "))
    hitung_luas_dan_keliling_lingkaran(jari_jari)
except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka.")
