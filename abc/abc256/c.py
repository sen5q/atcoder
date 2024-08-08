h1, h2, h3, w1, w2, w3 = map(int, input().split())

count = 0

for j in range(1,29):
    for k in range(1,29):
        for l in range(1,29):
            for m in range(1,29):

                a = j
                b = k
                d = l
                e = m
                c = h1-a-b
                f = h2-d-e
                g = w1-a-d
                h = w2-b-e
                i = w3-c-f

                if(h1==a+b+c)and(h2==d+e+f)and(h3==g+h+i)and(w1==a+d+g)and(w2==b+e+h)and(w3==c+f+i):
                    if(0<c<29)and(0<f<29)and(0<i<29)and(0<h<29)and(0<g<29):
                        #print(a,b,c,d,e,f,g,h,i)
                        count += 1

print (count)














