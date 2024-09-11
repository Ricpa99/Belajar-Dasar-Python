# list hampir sama dengan penggunaan array
# list adalah kumpulan data
# list bisa digunakan kumpalan data int str bool float

# kumpulan data number
angka = [1,2,3,4,5]
print(angka[4])
# kumpulan data string
string = ["winda sa", "salman ba", "bagas wa"]
print(string[2])

# kumpulan data bool
bol = [True, False, True, True]
print(int(bol[2]))

# cara alternatif membuat list menggunakan range
data = range(10)
lis = list(data)
print(data)
print(lis)

# lis menngunakan for
list_for = [i for i in range(1,10)]
print("lis for".center(15, "="))
print(list_for)

# lis menngunakan for dengan pangkat
list_for = [i**2 for i in range(1,10)]
print("lis for dengan pangkat".center(15, "="))
print(list_for)

# lis dengan menggunakan for dan if
lis_for_if = [i for i in range(10) if i !=2]
print("for lis menngunakan if :" , lis_for_if)

lis_for_if = [i for i in range(10) if i%2 ==0]
print("for lis modulus menngunakan if :" , lis_for_if)
lis_for_if = [i for i in range(10) if i%2 ==1]
print("for lis modulus menngunakan if :" , lis_for_if)

# contoh lis melihat berdasarkan index
data = ["agus" , "dewa", "iwan", "bayu", "ika pratiwi"]
a = int(input("masukkna data : "))
lis = data[a:4]
print(lis)

# contoh masuukan data ke list
lis = [0]
a = str(input("masukan nama :"))
lis.insert(2, a)
print(0 in lis)


