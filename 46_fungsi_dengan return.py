
# function normal
def pangkat(a):
   hasil = a**2


print(pangkat(5))

# fungsi dengan banyak return
def aritmatika(a,b):
   tambah = a + b
   kurang = a - b
   kali = a * b
   bagi = a / b

   return  kurang, kali, bagi, tambah


a,b,c,d = aritmatika(4, 3)
print(a)