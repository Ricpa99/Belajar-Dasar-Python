var = 9

coun = 1
print('menngunkana for'.center(9, "="))
for i in range(var):
    print(coun * "*")
    coun +=1


print('menngunkana while'.center(9, "="))
nilai = 1
while True:
    print(nilai * "*")
    nilai += 1

    if nilai > var:
        break

print('ketupat menggunkana while'.center(9, "="))
nilai = 1
geser = int(var/2)
while True:
    if (nilai % 2):
        print(" " *geser, "+" * nilai)
        geser -= 1
        nilai += 1
    else:
        nilai += 1
        continue
        
    if nilai > var:
        break


print("end")

