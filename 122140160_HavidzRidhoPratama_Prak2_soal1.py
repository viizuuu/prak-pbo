class Mahasiswa:
    def __init__(self, nim, nama, angkatan, isMahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.__angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    def get_angkatan(self):
        return self.__angkatan

    def get_isMahasiswa(self):
        return self.__isMahasiswa

    def method1(self):
        # Contoh method 1
        return f"{self.__nama} memiliki nim {self.__nim}"

    def method2(self, value):
        # Contoh method 2
        return f"{self.__nama} memiliki angkatan {self.__angkatan} dan nilai {value}"

    def method3(self):
        # Contoh method 3
        if self.__isMahasiswa:
            return f"{self.__nama} adalah mahasiswa"
        else:
            return f"{self.__nama} bukan mahasiswa"


# Membuat objek pertama dengan semua parameter
mahasiswa1 = Mahasiswa("123456", "John Doe", 2022)

# Membuat objek kedua tanpa parameter isMahasiswa (menggunakan default)
mahasiswa2 = Mahasiswa("654321", "Jane Smith", 2023)

# Memanggil method pada objek pertama
print(mahasiswa1.method1())
print(mahasiswa1.method2(90))
print(mahasiswa1.method3())

# Memanggil method pada objek kedua
print(mahasiswa2.method1())
print(mahasiswa2.method2(85))
print(mahasiswa2.method3())
