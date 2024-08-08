import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


h, w = map(int, input().split())
si, sj = map(int, input().split())
c=[]

wall = "##" + "#" * w

c.append(wall)

for i in range(h):
    c.append( "#" + input() + "#" )

c.append(wall)

x = input()



for i in range( len(x) ):

    #print(i, x[i], si, sj, end=" -> ")

    if ( x[i] == "L" ) and ( c[si][sj-1] == "." ):
            sj -= 1
    
    if ( x[i] == "R" ) and ( c[si][sj+1] == "." ):
            sj += 1

    if ( x[i] == "U" ) and ( c[si-1][sj] == "." ):
            si -= 1
    
    if ( x[i] == "D" ) and ( c[si+1][sj] == "." ):
            si += 1
    
    #print( si, sj )

print(si, sj)