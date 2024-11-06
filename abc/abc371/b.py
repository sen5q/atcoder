import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n,m = map(int, input().split())
o = [input().split() for _ in range(m)]
a = []
b = []
taro = [True] * (n+1)
for i in range(m):
    a.append(int(o[i][0]))
    b.append(o[i][1])


for i in range(m):

    if b[i] == "M":

        if taro[ (a[i]) ] == True:
            print("Yes")
            taro[ (a[i]) ] = False
            continue

        else:
            print("No")
            continue

    else:
        print("No")