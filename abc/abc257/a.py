import math

n, x = map(int, input().split())

ans = math.ceil(x/n)
ans = chr(ans + 64)

print(ans)