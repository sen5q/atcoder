import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

x = input()

while(1):

    if x[-1] == ".":
        x = x[:-1]
        print(x)
        exit()

    if x[-1] == "0":
        x = x[:-1]

    else:
        print(x)
        exit()