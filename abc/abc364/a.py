import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n = int(input())
s = [input().split() for _ in range(n)]
s.append("end")

for i in range(n-1):

    if ( (str(s[i])[2:7])=='sweet' ) and ( (str(s[i+1])[2:7]) =='sweet' ):

        #print(i, s[i], s[i+1], s[i+2])

        if(s[i+2] == "end" ):
            print("Yes")
            exit()
        else:
            print("No")
            exit()

print("Yes")