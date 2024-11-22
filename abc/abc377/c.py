import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n,m = map(int, input().split())
knight = [list(map(int, input().split())) for _ in range(m)]
unsafe = [[]]
p = unsafe.pop(0)

#ナイトが行けるマスの座標を記録
for i in range(m):
    unsafe.append( [knight[i][0], knight[i][1]] )
    unsafe.append( [knight[i][0]+2, knight[i][1]+1] )
    unsafe.append( [knight[i][0]+1, knight[i][1]+2] )
    unsafe.append( [knight[i][0]-1, knight[i][1]+2] )
    unsafe.append( [knight[i][0]-2, knight[i][1]+1] )
    unsafe.append( [knight[i][0]-2, knight[i][1]-1] )
    unsafe.append( [knight[i][0]-1, knight[i][1]-2] )
    unsafe.append( [knight[i][0]+1, knight[i][1]-2] )
    unsafe.append( [knight[i][0]+2, knight[i][1]-1] )

#重複を排除
unsafe = list(map(list, set(map(tuple, unsafe))))

#置けるマスを計算 unsafeリストの座標が盤面の中ならsafeを減らす
safe = n**2

for i in range (len(unsafe)):
    if( 1<= unsafe[i][0] <=n ) and ( 1<= unsafe[i][1] <= n):
        safe -= 1

print(safe)