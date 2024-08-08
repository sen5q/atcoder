n, q = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(q)]

ball = list(range(n))
for i in range(n):
    ball[i] = int(i)

###
for jj in range(n):
    j = int(jj)
    temp = ball[int(x[j])]
    ball[x[j]]   = ball[x[j]+1]
    ball[x[j]+1] = temp

print(ball)
###