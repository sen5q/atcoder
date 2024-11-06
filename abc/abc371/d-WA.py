import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

from itertools import accumulate
from bisect import bisect_left
from bisect import bisect_right

n = int(input())
x = map(int, input().split())
p = map(int, input().split())
q = int(input())
lr = [map(int, input().split()) for _ in range(q)]
l, r = [list(i) for i in zip(*lr)]

x = list( map( int, x ) )
p = list( map( int, p ) )

acc = []
for i in range(n):
    acc.append (list(accumulate(p[i:])))

print(bisect_right( x, l[0] ))
print(bisect_left ( x, r[0] ))

l_num = bisect_right( x, l[0] )
r_num = bisect_left ( x, r[0] )