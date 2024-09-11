# program kalkulator

angka_1 = int(input("masukkan angka : "))
pilih = input("operator -, +, /, x, : ")
angka_2 = int(input("masukkan angka kedua : "))



if pilih == "-":
     hasil = angka_1 - angka_2
     print('total = ', hasil)
elif pilih == "x" or pilih == "*":
     hasil = angka_1 * angka_2
     print("total = ", hasil)
elif pilih == "+":
     hasil = angka_1 + angka_2
     print("total = ", hasil)
else:
     print("salah")