# nested list

# data = [
#     ["marwan", "170091", "teknik", "laki-laki"],
#     ["fila", "170092", "teknik", "perempuan"],
#     ["putra", "170093", "teknik", "laki-laki"]
# ]


data_0 = ["agung", "170091", "teknik", "laki-laki"]
data_1 = ["sakdia", "170092", "teknik", "perempuan"]
data_2 = ["agung", "170093", "teknik", "laki-laki"]

# data_0 = [0,4,6,2]
# data_1 = [9,2,4,6]
# data_2 = [1,8,5,3,]

berkas = [data_0, data_1, data_2]
# for loop in data:
#     print("data nama mahasiswa : ", loop[0])

# print(data[1])

# list dengan reference
""" note : 
1.list yang telah di copy akan berubah dengan yang aslinya jika list
data di ubah. harus menggunakan deepcopy() agar tidak berubah dalam penggunaan nested list
"""
from copy import deepcopy
print("list dengan ference".center(25, "="))
# data_copy = deepcopy(berkas)
data_copy = berkas.copy()
data_copy[0][1] = "197430"
print(berkas)
print(data_copy)