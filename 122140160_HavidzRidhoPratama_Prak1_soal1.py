def hitung_bilangan_ganjil(batas_bawah, batas_atas):
    # Mengecek apakah batas bawah atau batas atas kurang dari nol
    if batas_bawah < 0 or batas_atas < 0:
        print("Batas bawah dan atas yang dimasukan tidak boleh di bawah Nol")
        return
    
    # Inisialisasi jumlah bilangan ganjil
    total = 0
    
    # Iterasi dari batas bawah hingga batas atas
    for i in range(batas_bawah, batas_atas + 1):
        # Mengecek apakah bilangan ganjil
        if i % 2 != 0:
            print(i)
            total = i + total
    
    # Cetak jumlah bilangan ganjil
    print("Total : ", total)

# Menerima input dari pengguna
batas_atas = int(input("batas atas: "))
batas_bawah = int(input("batas bawah: "))

# Memanggil fungsi untuk menghitung jumlah bilangan ganjil
hitung_bilangan_ganjil(batas_bawah, batas_atas)
