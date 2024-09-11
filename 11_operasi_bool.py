# operasi boolean di python : not, or, and, xor(^)
a = False
c = not a
print('Data a :', a, '\n', 'Not :', c)

# operasi and akan true jik salah satu aja true dan false jika ada satu aja flase
a = True
b = False
c = False
d = True
hasil = a and b and c and d
print(a, 'and', b, '=', hasil)

# operasi or akan benar semua jika satu aja true dan false sama false
a = True
b = False
c = False
d = False
hasil = a or b or c or d
print(a, 'or', b, '=', hasil)

# operasi xor/^ akan false jika semua true dan false jika keduanya true,
# dan jika jika salah satunya true maka akan true
a = True
b = True
c = True
d = False
hasil = a ^ b ^ c ^ d
print(a, '^', b, '=', hasil)
