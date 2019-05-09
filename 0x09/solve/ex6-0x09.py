import hashlib
deviceid = 999999910000000
for i in range(0, 100000000):
    text = str(deviceid+i)
    check = hashlib.sha256(text).hexdigest()
    print i
    if check == "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5":
        print text
        break   