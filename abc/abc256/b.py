import numpy as np

n = int(input())
a = list(map(int, input().split()))

p = 0

x = np.array([0])

for i in range(n):
    x = np.append(x, 0)
    x = x + a[i]

for i in range(len(x)):
    if( x[i] >= 4 ):
        p += 1

if( x[0] >= 4 ):
    p -= 1

print(x)