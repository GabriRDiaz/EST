f = open("ages.txt", "r")
lines = f.readlines()

years = []
for line in lines:
    years.append(str(line.split(" ")[0]))

with open('./ages.csv', 'w') as w:
    for y in years:
        w.write(y+";")
