# mengambil key dari data dictianari

data = {
   "nama": "agung",
   "alamat": "medan",
   "umur": 20,
   "jurusan": "teknik"
}

Data = [
   ["agung", "santi", "agung"]
   # ["bima", "sandar"]
]

# loop data dictionari dengan standart
for key in data:
   print(key)


# loop data dictionari menngunkana methode key()
# key1 = data.keys()
for index, key in enumerate(data.keys()):
   print("loop menggunakan methdoe key : ", index, "=", key)


# loop data dictionary menggunakan methode value(), items(), untuk melihat isinya
key2 = data.values()
key_a = data.items()
for key, val in data.items():
   print("key :", key, "\nvalues :", value)
   # print(f"key : {key} value : {value}")

