n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


max = max(a)

for i in range(len(a)):
    for j in range(len(b)):

        if(max==a[i])and(i+1==b[j]):
            print("Yes")
            exit()

print("No")