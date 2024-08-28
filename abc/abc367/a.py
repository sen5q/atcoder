import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

a, b, c = map(int, input().split())

if b<c:
    if b<a and a<c:
        print("No")

    else:
        print("Yes")


if b>c:
    if b<a or a<c:
        print("No")

    else:
        print("Yes")