import datetime
from collections import Counter
dt =  datetime.datetime.now()

print(f"tanggal hari ini : {dt}")
print(f"data waktu {dt.strftime('%A')}")

Data = ["a", "a", "r", "d", "d"]
jumlah = Counter(Data)
print(f"jumlah a {jumlah['a']}")

import io

buat = io.open("data.txt", "w")
a = 'hii there'
b = buat.write(a)
buat.close()
file = open("data.txt","r")
con = file.read()
print(f"baca file eksternal :  {b}")
print(f"baca file eksternal :  {con}")
file.close()