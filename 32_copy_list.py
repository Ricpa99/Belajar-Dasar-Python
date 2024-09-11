# cara duplicat data list

file = ["fahri", "tiara", "saipul", "bambang", "arif"]
print("data :", file)
file.sort()
print("data di sort:", file)

a = file
a[2] = "salman"
print("data file a".center(24, "="))
print(a)
print(file)
print("data file di copy".center(25, "="))
data = file.copy()
data[2] = "mahrum"
print(f"data : {file}")
print(f"data : {a}")
print(f"data : {data}")
file_my = ["fahri", "tiara", "saipul", "saipul", "bambang", "arif"]
# jumlah = file_my.count("a")
print("data : ", file_my.count("saipul"))