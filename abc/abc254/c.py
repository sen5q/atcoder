n, k= map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(n):
    for j in range(n-i-1):

        if a[j] > a[j+1]:
            count += 1
            a[j], a[j+1] = a[j+1], a[j] 



'''

1 5 6 7 8


'''