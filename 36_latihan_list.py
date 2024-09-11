# darftar buku dari list membuat DB sederhana

print('Program input data penulis buku'.center(25, "="))



Buku = []
while True:
   judul = input("Masukkan judul buku : ")
   penulis = input('Masukkan nama penulis : ')
   thun = input("Masukkan tahun terbit : ")

   Buku_baru = [judul,penulis,thun]
   Buku.append(Buku_baru)
   print("Data yang anda masukkan".center(19, "="))
   print(f"index\t\t\t | Judul buku\t\t\t | Nama punulis\t\t\t | Tahun terbit")
   for index, buku in enumerate(Buku):
      print(f"{index}\t\t\t | {buku[0]}\t\t\t | {buku[1]}\t\t\t | {buku[2]}")


   a = input("lanjutkan [y/n] : ")
   if a == 'y':
      continue
   else:
      break


print("terimakasih")
