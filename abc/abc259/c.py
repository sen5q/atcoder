def check1(a):
    b = list()

    i = 1
    while 1:

        if (a[i]!=a[i-1]) and (a[i]!=a[i+1]):
            b.append(a[i])
            b.append('1')

        if a[i] == a[i+1]:
            j = 1
            while 1:
                if( i==len(a)-2 ):
                    break
                
                if a[i] == a[i+1]:
                    i += 1
                    j += 1
                else:
                    break
            b.append(a[i])
            b.append('2+')
        
        i += 1

        if( i==len(a)-1 ):
            break

    return b




def check2(a):
    b = list()

    i = 1
    while 1:

        if (a[i]!=a[i-1]) and (a[i]!=a[i+1]):
            b.append(a[i])
            b.append('1')

        if a[i] == a[i+1]:
            j = 1
            while 1:
                if( i==len(a)-2 ):
                    break
                
                if a[i] == a[i+1]:
                    i += 1
                    j += 1
                else:
                    break
            b.append(a[i])
            b.append(str(j))
        
        i += 1

        if( i==len(a)-1 ):
            break

    return b



s = input()
t = input()

s = '0' + s + '0'
t = '0' + t + '0'

s1 = check1(s)
t1 = check1(t)
s2 = check2(s)
t2 = check2(t)


#print(s, t)
#print(s1)
#print(t1)
#print(s2)
#print(t2)

flag = True 
if( s1 == t1 ):

    i = 1

    while 1:

        if( int(s2[i]) == 1 ):
            if( s2[i] != t2[i] ):
                flag = False
                break
        
        if( int(s2[i]) >= 2 ):
            if( int(s2[i]) > int(t2[i]) ):
                flag = False
                break

        
        if( i == len(s2)-1 ):
            break

        i += 2

else:
    flag = False



if(flag):
    print("Yes")
else:
    print("No")