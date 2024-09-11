# macam - macam komparasi : <, >, <=, >=, ==, !=, is, is not

# komparasi is
a = 5
b = 5
hasil = a is b
print('nilai a =', a, 'id = ', hex(id(a)))
print('nilai b = ', b, 'id = ', hex(id(b)))
print('hasil = ', hasil)

a = 5
b = 5
hasil = a is not b
print('nilai a =', a, 'id = ', hex(id(a)))
print('nilai b = ', b, 'id = ', hex(id(b)))
print('hasil = ', hasil)

if a is not b:
    print('ok')
else:
    print('no')
