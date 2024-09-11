import datetime

Mahasiswa1 = {
   "nim": 170001,
   "nama": "putri ayu",
   "jurusan": "Teknik",
   "beasiswa": True,
   "tgl": datetime.date(1999,9,8)
}

Mahasiswa2 = {
   "nim": 170002,
   "nama": "putri melati",
   "jurusan": "Mesin",
   "beasiswa": True,
   "tgl": datetime.date(1999,1,3)
}

Mahasiswa3 = {
   "nim": 170003,
   "nama": "elvira putri",
   "jurusan": "elektro",
   "beasiswa": False,
   "tgl": datetime.date(1999,6,1)
}



DB = {
   "Data1": Mahasiswa1,
   "Data2": Mahasiswa2,
   "Data3": Mahasiswa3,
}  


print("Daftar Nama Yang Dapat Beasisiwa".center(30, "="))
print(f"{'key':<15} {'Nim':<10} {'Nama':15} {'Jurusan':<15} {'Beasiswa':15} {'Tgl':<15}")

for i, key in DB.items():
   print(f"{i:<15} {key['nim']:<10} {key['nama']:<15} {key['jurusan']:<15} {key['beasiswa']:<15} {key['tgl'].strftime('%x')}")  