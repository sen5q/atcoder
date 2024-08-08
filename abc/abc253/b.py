h, w = map(int, input().split())

s = [input().split() for _ in range(h)]


a = [-1,-1]
b = [0,0]


for i in range(h):
    for j in range(w):

        t = ''.join(s[i])
        if( t[j] == "o" ):

            if( a[0] == -1 ):
                a = [i,j]       #1,3
            else:
                b = [i,j]       #2,1


print( abs(a[0]-b[0]) + abs(a[1]-b[1]) )