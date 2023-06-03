import numpy as np
f = open("Outliers41.csv", "r")
lines = f.readlines()

values=[]
for line in lines:
    if(float(line.replace(',','.').strip())>(-150) and float(line.replace(',','.').strip())<130):
        values.append(float(line.replace(',','.').strip()))

arr = np.asarray(values)
arr.tofile('./ResidualsNoOutliers41.csv', sep = ';')  

