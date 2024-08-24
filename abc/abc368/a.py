import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

n, k = map(int, input().split())
a = list(map(int, input().split()))

j = len(a)-k        #最初に出力する位置

for i in range(n):

    if j == n:      #元の山の最後まで来たら最初に戻す
        j = 0

    print (a[j], end = ' ')

    j += 1