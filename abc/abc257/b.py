n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))



for i in range(q):
    flag = 1
    #print(a,l,i)
    selectpawn = a[l[i]-1]

    for j in range(k):
        if a[j] == selectpawn+1:
            flag = 0
    
    if selectpawn == n:
        flag =0

    if flag == 1:
        #print(a,l,i)
        a[l[i]-1] += 1

a_str = [str(i) for i in a]
print(' '.join(a_str))