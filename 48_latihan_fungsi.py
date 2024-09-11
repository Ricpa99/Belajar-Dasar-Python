# latihan fungsi
def hed():
   ''' header '''
   print(f"{'PROGRAM HITUNG LUAS DAN':^35}")
   print(f"{'PERSEGI PANJANG':^35}")
   print(35 * '-')


def user():
   lebar = int(input("Masukkan lebar : "))
   Panjang = int(input("Masukkan panjang : "))

   return lebar, Panjang

def func(p,l):
   luas = p * l
   keliling = 2 * (p + l)
   return luas, keliling

def show(luas, keliling):
   ''' menampilkan hasil '''
   print(f"hasil luas : {luas} \nhasil keliling {keliling}")




hed()
l,p = user()
luas, keliling = func(p, l)
show(luas, keliling)