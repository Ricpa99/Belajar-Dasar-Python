#dictionari

datadic = {
   "nama": "santo",
   "nim": 17001,
   "jurusan": 'teknin',
   "umur": 20,

   "per1": ["agung", "winda", "imah"]
}

# update data tidak bisa digunakan di lis hanya bisa di dcitionary
Data = ["sanjaya", "teknik", "tembung", 90]
datadic.update({"per2":["santo"]})
print(datadic)


# cara mengecek key di data dictionari menggunakan in
print("cara cek key di data dictionary".center(100,"="))
cek = "nama" in datadic
print(f"cek nama: {cek}")


# cara melihat panjang data dictionary


lent = len(datadic)
print('panjang data dictionary: ', lent)

# cara cek key di data dictionary menggunakan get
print("cara cek key di data dictionary menngunakan get".center(100,"="))
print(f'cek apakah ada : {datadic["nama"]}')
print(f'cek apakah ada {datadic["nama"]} : {datadic.get("nama")}')
print(f'cek apakah ada {datadic["nim"]} : {datadic.get("nim", "nama tidak ada")}')

# cara update data dictionary
print("update data dengan cara menual".center(100,"="))
print("cara update data dictionary".center(20, "="))
datadic["nama"] = "santi"
print("sebelum di update: ",datadic)
print("telah di update: ",datadic)

# cara update data dictionary make methode update
print("cara update data dictionary make methode update".center(100,"="))
datadic.update({"umur": 2})
print("update terbaru make methode: ", datadic)

datadic.update({"peserta1": "bagas"})
print(datadic)
del datadic["umur"]
print("nama peserta dihapus" ,datadic)