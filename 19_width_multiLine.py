# width dan multi line

nama = "agus bima sanjaya"
tinggi = 175
umur = 22
alamat = "medan"
jbatan = "karyawan"

print("Data String".center(20, "="))
# string standart
print(f" nama : {nama}\n tinggi : {tinggi}\n umur : {umur}\n alamat : {alamat}")

print("Data String".center(20, "="))
# string multilane
data = f"""
nama = {nama}
tinggi = {tinggi}
umur = {umur}
alamat = {alamat:<5} {jbatan}
"""
print(data)