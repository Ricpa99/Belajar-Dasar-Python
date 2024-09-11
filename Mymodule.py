
# def tambah(*args):
#    a = 0
#    for i in args:
#       a += i
#       return a

# def show(par):
#    return print(f"My name {par}")

# def pangkat(arsg):
#    return lambda a: a**arsg

# p = lambda a: a**2


import time

print(time.strftime("%Y-%m-%d/%r %z"))


a = int(input("no: "))
nim = "data"
nama = "nadia"
umur = 22


def func(*args, **kwarg) -> data:
   ''' nama mahasiswa '''
   return kwarg["file"], args[1] 


print(func(nim, nama, umur, file=a))