s = input()
i = 0

ans = ""

while True:
    if(len(ans) == 6): 
        break
    else:

        if(i==len(s)):
            i = 0
        
        ans += s[i]

        i += 1

print(ans)