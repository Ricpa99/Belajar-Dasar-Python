# excepton akan berjalan saat run time program mengalami error


# contoh exception
zero = "input yang benar"
val = "anda harus memasukkan angka"
type = "nilai yang adan masukkan salah"

try:
   user  = "ricky"
   pas = 20

   in_user = str(input("masukkan username: "))
   in_pas = int(input("masukkan digit: "))

   if in_user != user:
      print("user salah")
   elif in_pas != pas:
      print("pas salah")
   hasil = 10 / 0
except:
   # print(t)
   print(TypeError(type))
