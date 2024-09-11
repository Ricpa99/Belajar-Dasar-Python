# continue, pass
# pass tidak akan dieksekusi langsung di lewati

# contoh pas
# i = 1
# while i < 8:
#      i+=1
#      print("statmen pass")
#      if i == 4:
#           # print("statmen pass dalam if")
#           pass

# contoh continue
i = 0
while i <= 8:
    i +=1
    print(f"nilai i : {i}")

    if i == 4:
        print(f"nilai if i : {i}")
        continue
        # break
    print(5 * "=")
    print("lanjut")
