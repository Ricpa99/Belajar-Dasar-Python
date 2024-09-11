# type hints

# type hint berfungsi untuk mnedeklarasi tipe data di parameter
def hints(a):
   ''' fungsi normal'''
   return a**2

# contoh penngunaan type hints
def hins(a:int)->int:
   '''input integer'''
   return a**2

out = hints(8)
print(out)
out = hins(12.6)
print(out)