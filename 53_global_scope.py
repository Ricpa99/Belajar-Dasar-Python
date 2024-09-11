# contoh penggunaan varibel global
''' 
1.variabel global dapat di akses dimanapun 
2.variabel local hanya bisa di akses di dalam fungsi
3.variabel local dan global dapat di akses oleh for dan if dan while

'''

#var global bisa dipanggil dimanapun
var_global = "me Global"
# variabel dlama scope
def Local_scope():
   var_scope = "me Scope"

# memanggil var scope
''' maka tidak akan ditemukan '''
# print(var_scope) 


def func():
   print(f"memanggil variabel global dalam fungsi > {var_global}")

func()

# akses variabel global dalam loop
for i in range(3):
   print(f"memnaggil variabel global dalam for -> {var_global}") 

# dalam penggunaan percabnagn/kontrol flow

if True:
   print(f"memanggil variabel global dalam if -> {var_global}")

''' mengubah variabel global dalam if '''
print("ubag variabel global".center(30, "="))
glo_nilai = 0
print(glo_nilai)
if True:
   glo_nilai = 2
   print(f"mengubah var_glob dalam if {glo_nilai}")
print(glo_nilai)

''' mengubah variabel global dalam for '''
angka = 0
print(angka)
for i in range(4):
   angka += 3
   print(f" variabel glob : {angka}")
print(angka) 

''' mengubah variabel global dalam while '''
lok = 0
while lok < 3:
   lok += 1
   glo_nilai = 4
   a = "hello"
   def file():
      c = 10 # ini contoh variabel lokal dalam fungsi
      return c
   print(f"ubah var_glob dalam while : {glo_nilai}")

print(file())
print(f"ubah dalam while : {glo_nilai}")

''' mengubah variabel global dalam fungsi '''
print(f"nilai global -> {glo_nilai}")
def Myfuc(var):
   global glo_nilai
   glo_nilai = var
   return glo_nilai

print(f"sebelum : {glo_nilai}")
Myfuc(1)
print(f"ubah : {glo_nilai}")