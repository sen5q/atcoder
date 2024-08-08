n, w = map(int, input().split())
a = list(map(int, input().split()))

mid      = list(range(0))
midcheck = list(range(w+1))
anscheck = list(range(w+1))

for i in range(w+1):
    midcheck[i] = 0
    anscheck[i] = 0

ans = 0

if n==1:
    if(a[0] <= w):
        ans = 1

if n==2:
    if a[0]==a[1]:
        if a[0] <= w:
            ans = 1
    else:
        if a[0] <= w:
            print("0")
            ans += 1
        if a[1] <= w:
            print("1")
            ans += 1
        if a[0]+a[1] <= w:
            print("01")
            ans+=1



# if n>=3
w += 1

#1
for i in range(n):
    if(a[i] < w):
        anscheck[a[i]] = 1


#2
for i in range(n):
    for j in range(n):
        sum = a[i] + a[j]
        if((sum <= w) and (i!=j)):
            anscheck[sum] = 1



#3
for i in range(n):
    for j in range(n):
        sum = a[i] + a[j]
        if(sum <= w) and (i!=j):
            midcheck[sum] = 1

for i in range(w):
    if midcheck[i] == 1:
        mid.append(i)

for i in range( len(mid) ):
    for j in range(n):
        sum = mid[i] + a[j]
        if(sum < w):
            anscheck[sum] = 1

for i in range(w):
    if anscheck[i] == 1:
        ans += 1


print(ans)