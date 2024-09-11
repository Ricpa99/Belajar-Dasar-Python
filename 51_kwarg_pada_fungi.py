''' kwargs fungsi menggunakan dua bintang'''

def fungsi(nama,  nim, jurusan, alamat):
   ''' fungsi biasa '''
   print(nama,nim,jurusan,alamat)
fungsi("agus", 20, "teknik", "medan")

def kwargs(**par1):
   ''' fungsi kwargs '''
   # bisa juga mengnabil kye dengan memasukkan ke dalam variabel
   '''nama = par1["nama"]
   nim = par1["nim"]
   jurusan = par1["jurusan"]'''
   print(par1["nama"], par1["nim"], par1["jurusan"])
# kwargs dalam bentuk dictionary unutk menganmbil berdasarkan key
kwargs(nama = "nama", nim = 12, jurusan = "teknik")


def math(*args, **kwargs):
   out = 0
   if kwargs["opsi"] == "ok":
      for angka in args:
         out += angka
   elif kwargs["opsi"] == "kali":
      out = 1
      for angka in args:
         out *= angka
   else:
      print("operasi tidak ada!!")
   return out

hasil = math(1,2,3,4, opsi = "ok")
print(f"hasilnya : {hasil}")
hasil = math(1,2,3,4, opsi = "kali")
print(f"hasil : {hasil}")


# contoh penggunaan **kwrargs
def login(**log):
   
   if log["name"] != "ric":
      print("user salah")
   elif log["pas"] != "admin":
      print("passw salah")

   print("welcome")

   

a = input("user : ")
b = input("pass : ")
login(name = a, pas = b)