''' 
1. beberapa penggunaan open file:
w -> akan overwrite / menghapus semau isi dalam file dan mengantinya yang baru
a -> akan menambahkan file dengan baris dibelakangya
r+ -> akan menimpa file berdasarkan panjang huruf

''' 

with open('data.txt', 'a', encoding='utf-8') as a:

   run = True
   while run:
      par = str(input("masukkan teks: "))
      rid = a.write(par + '\n')

      ok = str(input("lanjut[y/n]: "))
      if ok == "y":
         continue
      else:
         run = False
      