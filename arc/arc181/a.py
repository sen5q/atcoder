import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# case[0] = ( 5, [5,4,3,2,1] )
#print(case[0][0])       #文字数
#print(case[0][1][0])    #最初
#print(case[0][1][-1])   #最後


t = int(input().strip())
case = []
for _ in range(t):
    n = int(input().strip())
    p = list(map(int, input().strip().split()))
    case.append((n, p))


for i in range(t):
    ans = 2

    if( case[i][1] == sorted(case[i][1]) ):
        ans = 0


    if( ans == 2                    and
        case[i][1][0] == case[i][0] and
        case[i][1][-1]== 1):
        ans = 3


    if ans == 2:
        for j in range (case[i][0]):
            left =  case[i][1][0:j]
            right = case[i][1][j+1:case[i][0]]

            #print(j, sum(left) , int(len(left)  * (len(left) +1)/2))
            #print(j, sum(right), int( (len(right)* (len(right)+1)/2) + (case[i][0]-len(right))*len(right) ))

            if ( sum(left) == int( len(left) * (len(left) +1)/2 ) and
                 sum(right)== int( (len(right)* (len(right)+1)/2) + (case[i][0]-len(right))*len(right) )):
                ans = 1


    print(ans)