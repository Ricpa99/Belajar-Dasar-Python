# default argumen dengan  satu parameter
def hello(name = "Kamu"):
   print(f"Hello apa kabar {name}")

# langsung menggunakan inputan
hello("Putri")
# tidak menggunakan inputan
hello()

# defult argumen dengan dua parameter
def hello(name, say = "Semua"):
   print(f"hii apa kabar {name} {say}")

print(hello("guys"))
print(hello("teman", "sekalian"))

# default argument dengan key di paramter
def key_argumen(input1=1, input2=2, input3=3):
   return input1 + input2 + input3


# mengubah key di inputan
a = int(input("masukkan angka : "))
print("Hasil =  ", key_argumen(a,input3=a))