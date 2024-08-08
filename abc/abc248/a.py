s = "459230781"

i=0

while i<10:

    j=0
    flag = 0

    while j<9:
        if i == int(s[j]):
            flag = 1
        j += 1
    
    if flag == 0:
        print(i)
        break
    
    i += 1