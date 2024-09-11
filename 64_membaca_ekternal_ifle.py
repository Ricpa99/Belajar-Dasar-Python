# cara membaca eksternal file dengan cara lama

''' membuka file '''
# file = open('data.txt', 'r')
# membaca file eksternal perbaris maka akan memberi enter otomatis
# print(file.readline())
# untuk menghilangka enter dengan menambahkan ,end='' dibelakang methode
# print(file.readline())
# print(file.read())
# print(file.readlines())
# cara mengecek tipe file read atau write
# print(file.readable())
# menutup file
# file.close()
#mengecek file jika sudah ditutup

# cara membuka file dengan cara terbaru dengan menggunakan keyword with open()
''' 
dalam menggunakan with open tidak perlu di close karna akan close
sendiri jika program selesai dijalankan
'''

with open ('data.txt', 'r') as file:
   print(f"daftar nama mahasiswa".center(50, "="),"\n\n\n")
   read = file.read()
   print(read)
   print(f"apa file diclose {file.closed}")


print('end')
