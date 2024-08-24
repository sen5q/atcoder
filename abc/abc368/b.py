import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

# 素直に処理するだけ

n = int(input())
a = list(map(int, input().split()))

count = 0
a.sort(reverse=True)        #降順でソート

while(True):
    count += 1
    a[0]  -= 1
    a[1]  -= 1

    a.sort(reverse=True)    #降順でソート

    if(a[1]<=0):            #正の要素の個数が1つ以下=降順ソート後の2番目の要素が0以下
        break

print(count)