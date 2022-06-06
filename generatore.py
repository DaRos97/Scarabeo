import numpy as np
import sys

N = int(sys.argv[1])
filename = 'alfabeto.npy'

L = np.load(filename)
res = []
ns = []
#for n in range(N):
rng = np.random.default_rng()
a = rng.choice(len(L), size=N, replace=False)
for n in range(len(a)):
    ns.append(a[n])
    res.append(L[a[n]])

newL = []
for n in range(len(L)):
    if n not in ns:
        newL.append(L[n])
np.save(filename,newL)

#with open(filename, 'w'):
#    f.write(newL)

print(res)
