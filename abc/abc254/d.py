n = int(input())    # 1 ~ 20000

count = 0

for i in range(1,10000):
    squarenum = i*i

    for j in range(1, n+1):
        tmp = float(squarenum/j)
        if(tmp.is_integer() and j<=n and tmp<=n):
            count += 1
        #print(flag,squarenum,j,tmp)

print(count)