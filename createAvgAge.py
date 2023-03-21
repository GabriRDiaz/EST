f = open("avgAge.txt", "r")
lines = f.readlines()

years = []
for line in lines:
    if(line[:2]=="18"):
        print("dieciocho")
        years.append(21)
    elif(line[:2]=="25"):
        print("veinticinco")
        years.append(29.5)
    elif(line[:2]=="35"):
        print("treintaycinco")
        years.append(39.5)
    elif(line[:2]=="45"):
        print("cuarenta")
        years.append(49.5)
    elif(line[:2]=="55"):
        print("cincuenta")
        years.append(59.5)
    else:
        print("error")
with open('./avgAges.csv', 'w') as w:
    for y in years:
        w.write(str(y)+";")