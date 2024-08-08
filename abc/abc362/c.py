n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

pretotal = 0
ans = []
for i in range(n):
    ans.append(0)
canzero = False

for i in range(n):
    if( a[i][0]>0 and a[i][1]>0 ):
        pretotal += a[i][0] 
        ans[i] = a[i][0]

    if ( a[i][0]<0 and a[i][1]<0 ):
        pretotal += a[i][1]
        ans[i] = a[i][1]


if pretotal>0:

    for i in range (n):

        # 曖昧なやつについて
        if( a[i][0]<=0 and 0<=a[i][1]):

            #足すと0にできるなら
            if( (pretotal + a[i][0])<=0 ):
                ans[i] = (0-pretotal)
                canzero = True
                break
            #足してもまだ0にできないなら
            else:
                ans[i] = a[i][0]
                pretotal += a[i][0]

        if pretotal==0:
            canzero = True
            break


if pretotal<0:

    for i in range (n):
        # 曖昧なやつについて
        if( a[i][0]<=0 and 0<=a[i][1]):

            #足すと0にできるなら
            if( (pretotal + a[i][0])>=0 ):
                ans[i] = pretotal
                canzero = True
                break
            #足してもまだ0にできないなら
            else:
                ans[i] = a[i][1]
                pretotal += a[i][1]
        
        if pretotal==0:
            canzero = True
            break


if pretotal==0:
    canzero = True


ans = str(ans)
ans = ans.replace(',', '')


if(canzero):
    print("Yes")
    print(ans[1:-1])

else:
    print("No")
