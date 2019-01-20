""" for recursive 10 took me 5x10**-5 seconds, 20 .0058 took seconds, 40 took 87.5 seconds, and 80 never finished.
for the for loop 10 took me .000006 seconds, 20 took .00001 seconds, 40 took .0001 seconds and 80 took .0002 seconds.
They are roughly exponential for the recursive.
There was a significant difference past 27 iterations. """

from timeit import default_timer as timer
import numpy as np

def fibRecursive(n):
    if n == 0:
         return 0
    elif n == 1:
        return 1
    else:
        return fibRecursive(n-1) + fibRecursive(n-2)

     


for n in range(1,40):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibRecursive(n), timer() - start))

def fibForLoop(n):
    a = np.array(range(n+1),int)
    a[0]=0
    a[1]=1
    for i in range(2,n+1):
        a[i]=a[i-1]+a[i-2]
    return a[n]

for n in range(1,81):
    start = timer()
    print("f({0}) = {1} took {2} seconds.".format(n, fibForLoop(n), timer() - start))