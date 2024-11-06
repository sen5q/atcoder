import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import numpy as np

s = [input() for _ in range(8)]

s2 = np.zeros((8,8))

for i in range(8):
    for j in range(8):

        if s[i][j] == "#":

            for k in range(8):
                s2[i][k] = 1
                s2[k][j] = 1

print( np.size(s2) - np.count_nonzero(s2) )