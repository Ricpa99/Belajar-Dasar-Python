import os
import CRUD


if __name__ == "__main__":
    cek_os = os.name

    while True:
        os.system("cls") if cek_os == "nt" else os.system("clear")
        # cara cek sistem os
        title = 'SELAMAT DATANG DI PROGRAM DATABASE MAHASISWA'
        panjang = len(title)
        print(f"{'=' * panjang:^90}")
        print(f"{title:^90}")
        print(f"{'=' * panjang:^90}")
        # pilihan user
        CRUD.init()
        print(f"1. read data")
        print(f"2. create data")
        print(f"3. update data")
        print(f"4. delete data")
        try:
            user_select = int(input("select: "))
            if (user_select > 4):
                print("anda hanya dapat memilih 1 - 4")
                break
        except (ZeroDivisionError, ValueError):
            print("silahkan masukkan angka [1-4]")
            break

        # hasil pilihan user

        print(CRUD.red(), "\n") if user_select == 1 else False
        print(CRUD.crete(), "\n") if user_select == 2 else False
        print(CRUD.update(), "\n") if user_select == 3 else False
        print(CRUD.delete(), "\n") if user_select == 4 else False
        user_ok = input("apakah selesai [y/n]: ")

        # cek inputan user
        if (user_ok == "n" or user_ok == "N"):
            continue
        if (user_ok == "y" or user_ok == "Y"):
            break
        else:
            break


