# date & time
import datetime as dt
import calendar as cl

while True:
   print("Input Tgl Anda".center(35, "="), "\n\n")
   tanggal = int(input("Masukkan Tgl anda : "))
   bulan = int(input("Masukkan bulan anda : "))
   tahun = int(input("Masukkan tahun lahir anda : "))

   a = f"{tahun}-{bulan}-{tanggal}"
   print("tahun lahir anda : ", a)
   umur = int(input("masukkkan tahun sekarang : "))
   myUmur = umur - tahun
   print("umur anda : ", myUmur , "tahun")
   a = cl.month(tahun, bulan,)
   print(a)


