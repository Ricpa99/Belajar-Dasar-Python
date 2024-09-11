import numpy as np

objek = np.array([4,6,3,5,])
objek2 = [1,4,6,3,]

print(f"objek list : {objek}")
print(f"objek numpy : {objek2}")

# membuat kuadrat pada matrix
print(f"kuadrat list = {objek2*2}")
print(f"kuadrat menggunakan numpy = {objek**2}")
# membuat matrix
matrix = np.array([(2,4,7),(4,5,3),(2,4,7)])
print(f"matrix = {matrix}")
print(f"kuadratin matrix = {matrix**2}")
# membuat zero nilai akan menjadi 0
zero = np.zeros((2,2))
print(f"nilai zero = {zero}")
# membuat ones niai akan menjadi 1
ones_c = np.ones((2,2))
print(f"nilai ones = {ones_c}")

perhitungan = matrix + matrix**2 + 5
print(f"hasil perhitungan = {perhitungan}")

