import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


n, t, p = map(int, input().split())
l = list(map(int, input().split()))

l.sort()

if( l[-p] >= t):
    print(0)
    exit()

print( t-(l[-p]) )