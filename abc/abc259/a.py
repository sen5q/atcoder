n, m, x, t, d = map(int, input().split())

t0 = t- d*x

if x<=m:
    ans = t
else:
    ans = t0+(d*m)

print(ans)