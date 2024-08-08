n = int(input())

ans = str(n%100)

if(int(len(ans)) == 1):
    ans = '0' + str(n%100)

print( ans )