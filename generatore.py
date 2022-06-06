import numpy as np
import sys

N = int(sys.argv[1])
filename = 'alfabeto.npy'

L = np.load(filename)
res = []
ns = []
for n in range(N):
    a = np.random.randint(0,len(L))
    ns.append(a)
    res.append(L[a])

newL = []
for n in range(len(L)):
    if n not in ns:
        newL.append(L[n])
np.save(filename,newL)

#with open(filename, 'w'):
#    f.write(newL)

print(res)
