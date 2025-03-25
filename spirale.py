import math
import numpy as np
import matplotlib.pyplot as plt
tetaEnd = 4*math.pi
teta = 0


with open("spirale.dat", "w") as file: 
    for i in np.arange(0, tetaEnd, 0.1):
        r = 0.5 + i
        teta = i
        file.write(f"{math.cos(teta)*r} {math.sin(teta)*r}\n")
        print(f"{math.cos(teta)*r} {math.sin(teta)*r}")

x=[]
y=[]

with open("spirale.dat", "r") as file:
    for line in file:
        cords = line.split()
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))

plt.figure(figsize=(8,8))
mini = min(x+y)*1.2
maxi= max(x+y)*1.2
plt.xlim(mini,maxi)
plt.ylim(mini,maxi)
plt.plot(x,y)
plt.savefig("spirale.png")

