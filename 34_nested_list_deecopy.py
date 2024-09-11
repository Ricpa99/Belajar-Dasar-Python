# data list copy menngunakan deepcopy() denggan import copy

from copy import deepcopy

Data = [
    [0, 4, 6, 2, 4],
    [8, 2, 6, 8, 3],
    [9, 2, 5, 7, 2, ]
]

print("copy list tanpa merubah yang aslinya".center(95, "="))
print(f"data asli : {Data}")
for i in Data:
    print("angka awal : ", i[2])
print(f"macsddress data asli : {hex(id(Data))}")
data_copy = deepcopy(Data)
print(f"Data yang di copy : {Data}")
data_copy[0][1] = 90
Data[0][1] = 45
print(f"Data ubah : {data_copy}")
print(f"Data asli : {Data}")
for i in Data:
    print(f"Data asli : {i[1]}")

print(f"addres data asli : {hex(id(Data))}")
print(f"addres data copy : {hex(id(data_copy))}")
