f = open("os.txt", "r")
lines = f.readlines()

os = []

for line in lines:
    if("macOS" in line):
        os.append("Apple")
    elif("Windows" in line):
        os.Append("Windows")
    else:
        os.Append("Linux")
