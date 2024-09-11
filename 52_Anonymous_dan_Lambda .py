# cek = lambda a,b,: a != b 
# a = int(input("masukkan jumlah ulang :"))
# b = int(input("masukkan nilai : "))
# bol = int(cek(a,b))

# if bol == True:
#    print("benar")
# elif bol == False:
#    print("salah")
# else:
#    print("program tidak")
# obj = lambda nama: nama

# function/output = lamda parameter:expresion
#contoh penggunaan
# parameter bisa kebih dari satu
kuadrat = lambda a: a**2
print(kuadrat(8))

# sorting list dengan panjang 
Data = ["bima","salken","cintia","arif","agus"]
Data.sort()
print(f"list data : {Data}")
def data(nama):
   return len(nama)

Data.sort(key=data)
print(Data)

# sort list mennakan lambda
file = ["putri","siska","agung","arif","amar"]
# file = [9,5,3,7,0,2]
file.sort(key=lambda objk : len(objk))
print(f"sort lis menggunakan lambda : {file}")

# filter list menggunakan lambda


berkas = [1,2,7,7,9,9,3,4]
def fildata(obj):
   return obj<3
# hasil akan memfilter angka yg lebih kecil dari parameter
a = list(filter(fildata, berkas))
b = list(filter(lambda a: a>=2, berkas))
print(f" {a} \n{b}")
# hasil genap
genap = list(filter(lambda a: (a%2 == 0), berkas))
print(f"cetak hasil genap : {genap}")
# hasil genjil
ganjil = list(filter(lambda a: (a%2 != 0), berkas))
print(f"cetak hasil ganjil : {ganjil}")
# kelipatan 3
kelipatan = list(filter(lambda a: (a%3 == 0), berkas))
print(f"cetak hasil kelipatan 3 : {kelipatan}")

#anonymouse function
# menggunakan function biasa
def func(a,b):
   return a**b
print(func(2, 4))
# menngunakan function lambda
# currying <- haskel curry
''' function lambda dengan currying '''
''' cara mengubah fungsi menjadi lambda '''
def lamda(n):
   return lambda parm: parm**n

# variabel fungsi menjadi lambda
# tetapi tidak begitu practicle mending langsung lambda
a = lamda(2)
print(f"function menjadi lambda : {a(8)}") 
print(f"function menjadi lambda : {lamda(2)(5)}") 