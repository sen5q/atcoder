import numpy as np

n, a, b = map(int, input().split())

ans = 0

l = np.linspace(0, n, n)

for i in range(n):
    l[i] = i+1


i = 0
while(1):
    i += 1
    ia = i*a
    if( ia >= n ):
        break
    l[ia-1] = 0


i = 0
while(1):
    i += 1
    ib = i*b
    if( ib >= n ):
        break
    l[ib-1] = 0

print( int(sum(l) - n))