import numpy as np
import matplotlib.pyplot as plt

def piapprox(N):
    xlist = []
    ylist = []
    for i in range(N):
        x = np.random.uniform(0,2)
        y = np.random.uniform(0,2)
        xlist.append(x)
        ylist.append(y)

    outxlist = []
    outylist = []
    inxlist = []
    inylist = []
    for x,y in zip(xlist,ylist):
        if ((1-x)**2+(1-y)**2)**0.5 <= 1:
            inxlist.append(x)
            inylist.append(y)
        else:
            outxlist.append(x)
            outylist.append(y)
    area = (len(inxlist)/(len(outxlist)+len(inxlist)))*4
    return area

points = int(input("Enter number of points: "))
step = int(input("Enter step size: "))

inputvals = np.arange(1,points,step)
fractionalerr = []
for i in inputvals:
    fractionalerr.append(abs((np.pi-piapprox(i)))/np.pi)

f1, ax1 = plt.subplots()
ax1.plot(inputvals,fractionalerr)
ax1.set_xlabel("Number of points (N)")
ax1.set_ylabel("Fractional error")
ax1.set_title("Fractional error of Pi using Monte Carlo")
f1.show()

input("\nPress <Enter> to exit...\n")