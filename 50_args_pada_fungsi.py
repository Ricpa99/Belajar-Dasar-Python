# type fungsi tidak dengan keyword *args
# *args tipenya tuple dan dia bisa di iterasi

def func(nama,nim,jurusan):
   print(f"nama : {nama} nim : {nim} jurusan : {jurusan}")

func("dewa", 17, "ti")

def func(data_lis):
   a = data_lis.copy()
   nama = a[0]
   nim = a[1]
   jurusan = a[2]
   print(nama, nim, jurusan)

func(["ric", 12, "ti"])

# type fungsi menggunakan keyword *args

def func(*args):
   nama = args[0]
   nim = args[1]
   jurusan = args[2]
   print(nama, nim, jurusan)

func("baga", 2, "si")

def tambah(*data):
   out = 0
   for i in data:
      out += i
   return out

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)



# penggunaan *args tidak bisa dilakukan untuk semua inputan sekaligus
def daftar(*user):
   # name = user[0]
   # las = user[1]
   print(f"nama awal : {user} \nnama akhir : {use}")



a =str(input("masukkan nama awal : "))
b = str(input("masukkan nama akhir : "))
daftar(a,b)