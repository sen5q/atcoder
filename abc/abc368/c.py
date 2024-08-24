import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math

n = int(input())
h = list(map(int, input().split()))

t = 0

for i in range(len(h)):

    #どのターンからでも3ターンで5ダメージ
    t    += math.floor(h[i]/5)*3
    h[i]  = h[i]%5


    """ t(mod3)
        |   0   1   2
    ----+-----------
残HP4   |   3   2   2
    3   |   3   2   1
    2   |   2   2   1
    1   |   1   1   1 """

    if h[i] == 4:
        if   t%3 == 0:
            t+=3
        elif t%3 == 1:
            t+=2
        elif t%3 == 2:
            t+=2

    if h[i] == 3:
        if   t%3 == 0:
            t+=3
        elif t%3 == 1:
            t+=2
        elif t%3 == 2:
            t+=1

    if h[i] == 2:
        if   t%3 == 0:
            t+=2
        elif t%3 == 1:
            t+=2
        elif t%3 == 2:
            t+=1

    if h[i] == 1:
        t+=1



print(t)