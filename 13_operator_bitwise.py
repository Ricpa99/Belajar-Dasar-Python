
# operator bitwise: not,or,xor,and,shift rigth(>>/),left(<<)
a = 9
b = 5

# penggunan operator bitwise |, ~, &, ^, bebrbeda hasilnya dengan menggunakan bool or, not, and, xor
c = a | b
print('nilai a :', a, 'binary: ', format(a, '08b'))
print('nilai b :', b, 'binary: ', format(b, '08b'))
print('format |: ', c, 'binary: ', format(c, '08b'))

print(5 * '=')
c = a or b
print('nilai a :', a, 'binary: ', format(a, '08b'))
print('nilai b :', b, 'binary: ', format(b, '08b'))
print('format or: ', c, 'binary: ', format(c, '08b'))
