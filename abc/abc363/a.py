import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


r = int(input())


if (r<100):
    print( 100-r )

elif( r<200 ):
    print( 200-r )

elif( r<300 ):
    print( 300-r )