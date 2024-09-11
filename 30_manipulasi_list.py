# data lis
""" 1.jika mau melihat data list paling akhir atau melihat dari belakng mmenggunakan minus(-) dengan melihat panjang lis
    menngunakan methode len()
    2.melihat data berdarakan index dari 0 sampai seterusnya
    3.menambhkan data mengunakan insert objek.insert(index,objek)
"""

data_nama = ["mira", "agus", "bima"]

# print("jumlah data : ", data_nama.__len__())
# print("nama awal :", data_nama[1])
# print("nama ahkir :", data_nama[-1])
# a = input("masukkan data lis : ")
# data_nama.insert(0, a)
# print("tambah data lis : ", data_nama)
# a = input("masukkan data lis dengan append :")
# data_nama.append(a)
# print("tambah data lis : ", data_nama)
print("join data list".center(25))
data_baru = ["ika", "putri",]
data_nama.extend(data_baru)
print(data_nama)
a = input("hapus data lis baru : ")
data_nama.remove(a)
print(data_nama)
a = input("ubah nama :")
data_nama[1] = a
print(data_nama)
# hapus data list paling akhir bisa menggunakan methode .pop