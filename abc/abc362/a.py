r, g, b = map(int, input().split())
c = input()

if ( c=="Red" ):
    r = 200

if ( c=="Green" ):
    g = 200

if ( c=="Blue" ):
    b = 200

if( r<=g and r<=b ):
    print(r)
    exit()

if( g<=r and g<=b ):
    print(g)
    exit()

if( b<=r and b<=g ):
    print(b)
    exit()