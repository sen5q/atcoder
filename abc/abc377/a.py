import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

s = input()

ans = ('A' in s) and ('B' in s) and ('C' in s)

if ans == True:
    print("Yes")
else:
    print("No")