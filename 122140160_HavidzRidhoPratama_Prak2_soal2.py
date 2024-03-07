# Class pertama dengan decorator
class DecoratorExample:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Decorator Example: Sebelum eksekusi fungsi")
        result = self.func(*args, **kwargs)
        print("Decorator Example: Setelah eksekusi fungsi")
        return result

@DecoratorExample
def decorated_function():
    print("Fungsi yang didekorasi")

decorated_function()


# Class kedua dengan constructor dan destructor
class ConstructorDestructorExample:
    def __init__(self):
        print("Constructor Example: Objek dibuat")

    def some_method(self):
        print("Metode dijalankan")

    def __del__(self):
        print("Destructor Example: Objek dihapus")

# Membuat objek dari class kedua
obj = ConstructorDestructorExample()
obj.some_method()

# Menghapus objek
del obj
