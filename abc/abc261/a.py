l1, r1, l2, r2 = map(int, input().split())
ans = 0

if l1 < l2:
    if r1 < r2:
        ans = r1-l2
    
    else:
        ans = r2-l2

else:
    if r1 < r2:
        ans = r1-l1

    else:
        ans = r2-l1

if ans<0:
    ans = 0

print(ans)