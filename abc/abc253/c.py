n = int(input())
q = [input().split() for _ in range(n)]

s = []


for i in range(n):

    r = q[i]



    if(r[0] == '1'):
        s.append(int(r[1]))



    if(r[0] == '2'):
        count = s.count(int(r[1]))

        if( count < int(r[2]) ):
            numdelete = count
        else:
            numdelete = r[2]

        count = 0
        for j in range(numdelete):
            s.remove(int(r[1]))



    if(r[0] == '3'):
        print( max(s) - min(s) )