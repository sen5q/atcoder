n = int(input())

a = []
for i in range(n):
    inp = input()
    a.append(inp)


flag = 1

for i in range(n):
    for j in range(n):

        if i<j:

            if(   ((a[i][j] == 'W') and (a[j][i] != 'L'))
                or((a[i][j] == 'L') and (a[j][i] != 'W'))
                or((a[i][j] == 'D') and (a[j][i] != 'D'))   ):
                flag = 0


if flag == 1:
    print("correct")
else:
    print("incorrect")