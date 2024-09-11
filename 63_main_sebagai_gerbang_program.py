# __main__ adalah top level code environment

# __name__ == "__main__"


# __name__ pada file program utama

import __main__63 # -> cara memanggil package agar bisa berjalan di terminal 'python __main__63'

def fungsi(a):
   return a + 4




if __name__ == "__main__":
   print(fungsi(5))



