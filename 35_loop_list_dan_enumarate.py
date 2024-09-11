# loop list dengan for

Data = [9,5,8,3,6]


jumlah = len(Data)
print(jumlah)
for i in range(jumlah):
   print(f"data : {Data[i]} ")


for j in Data:
   print(f"berkas: {j}")


# menngunakan while
print("cara menngunakan while".center(20, "="))
i = 0
while i < jumlah:
   print(f"File : {Data[i]}")
   i +=1

# loop list menggunakan comprehension
print("prin list menggunakan compherensip".center(25,"="))
angka = [
   [19001, "wina salma", "teknik informasi",],
   [19002, "agus dol", "teknik informatika",],
   [19003, "sarah mina", "teknik sastra",]
   
   
   ]

[print(f"Nama : {i[2]}") for i in angka]

print("prin list menggunakan enumurate".center(25,"="))
# menggunakan enumerate
file = [
   [19001, "wina salma", "teknik informasi",],
   [19002, "agus dol", "teknik informatika",],
   [19003, "sarah mina", "teknik sastra",]
   ]

for index, berkas in enumerate(file):
   print(f"index : {index} \t nim : {berkas[0]} \t nama : {berkas[1]} jurusan : {berkas[2] }")

