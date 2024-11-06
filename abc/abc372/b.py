import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math

m = int(input())

i = 0
mod3 = [0,0,0,0,0,0,0,0,0,0,0]

while True:
    mod3[i] = m%3
    m = math.floor(m/3)

    if m<3:
        mod3[i+1] = m
        break

    i += 1

n = 0
ai = []

for i in range(11):
    if mod3[i] != 0:
        n += mod3[i]
        for j in range(mod3[i]):
            ai.append(i)

print(n)
print(*ai)