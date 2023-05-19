import numpy as np
import matplotlib.pyplot as plt

pointnum = int(input("Enter a number of points to plot: "))

xlist = []
ylist = []
for i in range(pointnum):
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

f1, ax1 = plt.subplots(figsize=(10,10))
ax1.scatter(outxlist,outylist)
ax1.scatter(inxlist,inylist)
ax1.set_title("Monte Carlo Circle")
circle = plt.Circle((1,1),1, color='orange', fill=False)
ax1.add_patch(circle)
ax1.set_ylim(0,2)
ax1.set_xlim(0,2)
f1.show()
area = (len(inxlist)/(len(outxlist)+len(inxlist)))*4
print(f"The area of the circle, and therefore value for pi, is approx. {area}")
input("\nPress <Enter> to exit...\n")
    
