a = list(map(int, input().split()))
b = a[1]

a.sort()


if( int(a[1]) == b ):
    print("Yes")
else:
    print("No")