# contoh import module
''' 1.cara import module menggunakan import '''
import Mymodule
''' 2.cara import moudule menggunakan from dengan 
memilih fungsi dan variabel yang ada di module yang di rekomendasikan'''
from Mymodule import tambah, pangkat, show
''' 3.cara i port module dengan menggunakan bintang yang artinya 
mengambil semua moddule yang ada di didalamnya '''
from Mymodule import *

a = Mymodule.pangkat(2) #cara mengambil  import module pertama
b = tambah(4,6,2,4,) #cara  mengambil import module yang kedua
c = show("ricky") #cara mengambil  import yang ketiga 