# copy data dictionary dan mengubahnya

dictio = {
   "dictio": "warman",
   "nim": 19001, 
   "jurusan": "teknik"
}

# copy data dictionary dengan cara seperti ini dapat merubah data dictionari asli
frend = dictio
print("data dictio = ", dictio)
print("data frend = ", frend)

# copy dictio menggunakan methode copy tidak dpat merubah data dictionari yang asli
frend = dictio.copy()
frend["dictio"] = "wanda"
print("data dictio = ", dictio)
print("data frend = ", frend)

# menggunakan methode pop() akan mengirim data dictionary ke varibael
kirim = dictio.pop("jurusan")
print(f"kirim data = {kirim}")
print("data frend = ", dictio)

# menggunkan methode popitem() untuk melihat data dictionary paling akhir

print(f"data dictionari yang paling akhir {frend.popitem()}")