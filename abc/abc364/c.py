import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n, amax, bmax = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

anow = 0
bnow = 0

for i in range(n):
    anow += a[-(i+1)]
    bnow += b[-(i+1)]

    if(anow>amax)or(bnow>bmax):
        print(i+1)
        exit()
    
print(n)