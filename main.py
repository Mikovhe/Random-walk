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
y = random.randint(1,L)
fig, ax = plt.subplots(1, 1)
for i in range(n):
    D = random.randint(1,4)

    if D ==1:
        x = x+1

    elif D==2:
        y = y+1

    elif D==3:
        x =x-1

    elif D==4:
        y = y-1

    plt.scatter(x,y)

#    print(x,y)

plt.show()
