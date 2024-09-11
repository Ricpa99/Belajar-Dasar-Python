import datetime
import os
import random
import string

Mahasiswa = {
   "nim": "default", 
   "nama": "default",
   "jurusan": "default",
   "beasiswa": "default",
   "tgl": "default",
}


DB = {
   
}  
os.system("cls")
while True:
   print("Input Data Mahasiswa".center(30, "="))
   Mahasiswa = dict.fromkeys(Mahasiswa)
   Mahasiswa['nim'] = input("nim : ")
   Mahasiswa['nama'] = input("nama : ")
   Mahasiswa['jurusan'] = input("jurusan : ")
   Mahasiswa['beasiswa'] = input("beasiswa : ")
   dd = int(input("input tgl lahir : "))
   mm = int(input("input bulan lahir : "))
   yy = int(input("input tahun lahir : "))
   Mahasiswa['tgl'] = datetime.date(yy, mm, dd).strftime("%x")

   print(f"{'key':<15} {'Nim':<10} {'Nama':15} {'Jurusan':<15} {'Beasiswa':15} {'Tgl':<15}")
   print(55 * '-')
   key = ''.join((random.choice(string.ascii_uppercase) for i in range(9)))
   DB.update({key:Mahasiswa})
   for key, value in DB.items():
      print(f"{key:<15} {value['nim']:<10} {value['nama']:<15} {value['jurusan']:<15} {value['beasiswa']:<15} {value['tgl']}")

   ok = input("lanjut [y/n] : ")
   if ok == "y":
      continue
   else:
      break

print("Data berhasil di input")