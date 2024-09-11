# format string
# bisa juga digunakan untul tpe data bool, str, int, float()

a = 'hasil '
# menngunkan varible float
b = 35000000
# c = int(input("masukkan nilai : "))
# print(c)
# print(f" {c:,}", a + str(b))

# menampilkan angka dibelakang koma bilanga decimal
a = 1784.73892
print(f'nilai decimal : {a:.4f}')

# menampilkan leading zero dengan cara menambahkan angka di depan titik
a = 784.829
print(a)
print(f'{a:00.1f}')

# menampilkan plus & minus 
a = -9.8508
b = 5.74639
print(f'minus : {a:-.2f}')
print(f'plus : {b:.2%}')
print('+9.82992')

# melakukan operasi aritmatika di placeholser
a = 1
b = 12
print('Total harga :', f'{a + b:,}')
print('Total harga :', f'{a % b:,}')

# menapilkan biner, octal, hexadecimal

a = 2
b = "saya"
print('nilai biner : ', f'{bin(id(a))}')
print('nilai hex : ', f'{hex(a)}')
print('nilai oct : ', f'{oct(id(b))}')
print('nilai format : ', format(a, '04b'))