f = open("avgAge.txt", "r")
lines = f.readlines()

years = []
for line in lines:
    if(line[:2]=="18"):
        years.append(21)
    elif(line[:2]=="25"):
        years.append(29.5)
    elif(line[:2]=="35"):
        years.append(39.5)
    elif(line[:2]=="45"):
        years.append(49.5)
    elif(line[:2]=="55"):
        years.append(59.5)
    else:
        print("error")
with open('./avgAges.csv', 'w') as w:
    for y in years:
        w.write(str(y)+";")