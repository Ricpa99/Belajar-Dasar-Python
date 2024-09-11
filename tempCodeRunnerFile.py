

if __name__ == "__main__":
    cek_os = os.name

    while True:
        os.system("cls") if cek_os == "nt" else os.system("clear")
        # cara cek sistem os
        title = 'SELAMAT DATANG DI PROGRAM DATABASE PERPUSTAKAAN'
        panjang = len(title)
        print(f"{'=' * panjang:^90}")
        print(f"{title:^90}")
        print(f"{'=' * panjang:^90}")
        # pilihan user
        CRUD.init()
        print(f"1. read data")
        print(f"2. create data")