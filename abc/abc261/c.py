n = int(input())

s = []
for i in range(n):
    inp = input()
    s.append(inp)

dic = {}

for i in range(n):

    name = str(s[i])

    if name in dic:
        print( name + "(" + str(dic[name]) + ")" )
        dic[name] = dic[name]+1

    else:
        tmpdic = { s[i]: 1 }
        dic.update( tmpdic )
        print( name )