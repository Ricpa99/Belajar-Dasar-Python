
file = "bagas, agung, bima"

"""nama = str(input("cari nama :"))
if nama in file:
    print(nama, 'ditemukan')
elif nama not in file:
    print(nama, 'tidak ditemukan')"""

# 1.menyambung pada string
nama_depan = "putra "
nama_belakang = "sanj\'aya"

nama_lengkap = nama_depan + '"' + nama_belakang
print(nama_depan)
# 2.melihat panjang pada string
count = len(nama_depan)
print('panjang nama :' + nama_lengkap, '=', str(count))
print('panjang nama :' + nama_depan[0])

# 3.mengecek huruf pada varibel
cek = "baru"
cekId = cek in nama_lengkap
print((cek + ' apakah ada = ' + str(cekId)))
cekId = cek not in nama_lengkap
print((cek + ' tidak ada = ' + str(cekId)))

# 4.melihat string berdasarkan index
# melihat rentang nama string dai mulai index 0
angka = 'makan bersama dengan teman'
nilai = angka.count('d')
print('nama di mulai : ' + file[0:14])
print('nama di mulai : ' + file[0:9:1])
print('melihat nama dari mulai belakang : ' + file[-1])
# 5.operator dalam bentok methode
print("nilai paling besar: " + max(file))
print("nilai paling kecil: " + min(file))
print("nilai huruf " + str(angka) + " = " + str(nilai))
