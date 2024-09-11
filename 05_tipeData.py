# macam - macam tipe data di python integer, float, bool, str, complex

# tipe data integer bilangan bulat
from ctypes import c_char, c_long, c_double, c_short
tipe_int = 15
print('data :', tipe_int, '\n' 'bertipe :', type(tipe_int))
# tipe data float bilangan koma
tipe_float = 22.9
print('data :', tipe_float, '\n' 'bertipe :', type(tipe_float))
# tipe data string adalah
tipe_string = "22.9"
print('data :', tipe_string, '\n' 'bertipe :', type(tipe_string))
# tipe data boolean adalah nilai biner 0 & 1/true & false
tipe_bool = 22.9
print('data :', tipe_bool, '\n' 'bertipe :', type(tipe_bool))

# tipe data khusus
tipe_khusus = complex(9.4)
print('data :', tipe_khusus, '\n' 'bertipe :', type(tipe_khusus))

# memasukkan tipe data c
c = "halo"
a = c_char(55)
print('data :', a, '\n' 'bertipe :', type(a))
