a = 10
b = 3
hasil = a + b
print(a, '+', b, '=', hasil)

# operasi eksponen (pangkat)
hasil = a ** b
print(a, '^', b, '=', hasil)

# operasi modulus 
hasil = a % b
print(a, '%', b, '=', hasil)

# operasi floor devision
hasil = a // b
print(a, '//', b, '=', hasil)

# priotas operasi
""" dijumlahkan berdasarkan urutan
1.()
2. eksponen/pangkat **
3.perkalian dan aritmatika yg lainnta *,/,**,%,//
4.pertambahan dan pengurangan - & +
"""

a = 15
b = 22.5
c = 7
hasil = a + b // c ** b - a / c * b % a
print(a, '+', b, '//', c, '**', b, '-', a, '/', c, '*', b, '%', a, '=', hasil)
