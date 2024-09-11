
#  nama.isalpha() <-- untuk mengecek semua huruf
#  nama.isalnum() <-- mengecek huruf dan angka
#  nama.isspace() <-- untuk mengecek spasi, tab dan new line
# nama.isdecimal() <-- untuk mengecek angka saja
# nama.istitle() <- untuk menegcek awal huruf besar semua

# mengubah nama ke kapital
nama = 'nama dalam bentuk kapital'
set = nama.upper()
print('contoh nama :' + set)


# mengubah nama ke ke huruf kecil
nama = 'nama dalam bentuk kecil'
set = nama.lower()
print('contoh nama :' + set)

# pengecekan nama menggunakan methode isX
# mengecek nama huruf besar atau kecil
nama = 'nama dalam bentuk kecil'
# pengecekan methode bisa digunakan di ahkir
a = 'masukkan nama'.islower()
set = nama.istitle()
print('cek dalam :' + str(a))
set = nama.islower()
print('cek karakter tidak kapital :' + str(set))

# ngecek komponen startswith() & endswith()
start = 'Manusia serigala didepan'.endswith('didepan')
print('cek methode start : ' + str(start))

# penggabungan menngunakan methode join/.join() dan spplit/.split
lis = ['frea', 'ira', 'mita', 'dewa']
listt = 'bagas', 'jaya', 'mardan'
print(lis)
# join = ' hah '.join(lis)
print('join lis : ' + ''.join(listt))

# penggunan join komponen methode .split mengembalikan ke dalam bentuk list
join = "hari yang begitu sibuk"
# print(join.split(' halo ')) tidak terlalu penting

# mengubha teks rata kana, kiri, dan tengah menngunakan .sleft
print('program kalkulator'.center(50, '='))
print('program kalkulator'.ljust(50, '='))
print('program kalkulator'.rjust(50, '='))

# menghilankan tanda di string menngunakan strip
tks = 'apa +  saja + yang + di + lakukan'
a = tks.center(45, '=')
strp = tks.strip("+")

print(tks)
print(' hasil :' + a)
print(' hasil :' + strp)