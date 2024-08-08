import math

n = int(input())
s = input()

count = 0
ans = 1

for i in range(n-1):
    count += 1
    if (s[i]==s[i+1]):
        #print("hit")
        ans *= math.ceil(count/2)
        count = 0
    #print("%3d, %3d, %5d" %(i, count, ans))

count += 1
ans *= math.ceil(count/2)

print(ans % 1000000007)