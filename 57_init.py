import package_init
from package_init.berkas import main
from package_init.berkas.data import apps


a = main.var_a
b = apps.hello("kalian")
print(a, "\n", b)