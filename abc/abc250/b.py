n, a, b =map(int, input().split())

flag = 0
flagbr = n*b
cntprint = 0
cntbr = 0

for h in range(n*n):
    for i in range(a):
        for j in range(b):

            if flag%2 == 0:
                print(".",end='')
                cntprint += 1
            else:
                print("#",end='')
                cntprint += 1

            if cntprint == flagbr:
                cntbr += 1
                cntprint = 0
                print("\n")

                if (n%2==1) and (cntbr%a!=0):
                    flag += 1
                if (n%2==0) and (cntbr%a==0):
                    flag += 1

        flag +=1