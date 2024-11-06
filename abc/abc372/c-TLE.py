import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n, q  = map(int, input().split())
s = input()
s = "xx" + s + "xx"

in_xc = [input().split() for _ in range(q)]

x = []
c = []

for i in range(q):
    x.append(int(in_xc[i][0]))
    c.append(in_xc[i][1])



ans = 0
for i in range(n+4):

    if s[i]=="A":
        if s[i+1]=="B":
            if s[i+2]=="C":
                ans +=1



for i in range(q):

    if s[x[i]+1] == c[i]:
        print(ans)
        continue

    if s[x[i]+1] == "A":
        if s[x[i]+2] == "B":
            if s[x[i]+3] == "C":
                ans -= 1

    if s[x[i]+1] == "B":
        if s[x[i]+2] == "C":
            if s[x[i]] == "A":
                ans -= 1

    if s[x[i]+1] == "C":
        if s[x[i]] == "B":
            if s[x[i]-1] == "A":
                ans -= 1


    if c[i] == "A":
        if s[x[i]+2] == "B":
            if s[x[i]+3] == "C":
                ans +=1

    if c[i] == "B":
        if s[x[i]+2] == "C":
            if s[x[i]] == "A":
                ans +=1

    if c[i] == "C":
        if s[x[i]] == "B":
            if s[x[i]-1] == "A":
                ans +=1

    s = s[:x[i]+1] +  c[i]  + s[x[i]+2:]

    print(ans)