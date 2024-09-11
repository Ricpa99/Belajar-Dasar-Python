# fungsi argume

def getName():
   print('fungsi dengan meapilkan string')

def tambah(a,b):
   hasil = a + b
   print(f"{a} + {b} hasil : {hasil:,}")

a = int(input("masukkan nilai awal : "))
b = int(input("masukkan nilai akhir : "))

tambah(a, b)