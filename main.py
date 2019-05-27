import sys

import random
import matplotlib.pyplot as plt
import numpy as np
#number of steps


random.seed(None)

#print "Input number of steps\n"

try:
    n = int(raw_input("Insert number of steps\n"))
except ValueError:
    print "Not a number"
    sys.exit(1)

try:
    L = int(raw_input("Insert length of box\n"))
except ValueError:
    print "Not a number"
    sys.exit(1)
x = random.randint(1,L)
x_init = x
y = random.randint(1,L)
y_init = y
fig, ax = plt.subplots(1, 1)
ax.plot(x,y,color = 'green',marker = 'o',linestyle = 'solid')
#print(x,y)

#some statistics
x_total = x
y_total = y

xcount = 0
ycount = 0

for i in range(n):
    D = random.randint(1,4)

    if D ==1:
        x = x+1
        x_total +=x
        xcount +=1

    elif D==2:
        y = y+1
        y_total +=y
        ycount +=1

    elif D==3:
        x =x-1
        x_total +=x
        xcount += 1

    elif D==4:
        y = y-1
        y_total += y
        ycount +=1

    #print(x,y)
    ax.plot(x,y,color = 'black', marker = '*',linestyle = 'solid')

ax.plot(x,y,color = 'red',marker = 'o',linestyle = 'solid')
#    print(x,y)
print(x_total,y_total,x_total/xcount+y_total/ycount,xcount,ycount)

plt.savefig("random")
plt.show()
