import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

def remove_repetition(iterable):
    result = []
    for item in iterable:
        if item not in result:
            result.append(item)
    return result

n, k = map(int, input().split())
r = list(map(int, input().split()))

alllist = [[9,9,9,9,9,9,9,9]]
anslist = [[]]

for i1 in range(5):
    for i2 in range(5):
        for i3 in range(5):
            for i4 in range(5):
                for i5 in range(5):
                    for i6 in range(5):
                        for i7 in range(5):
                            for i8 in range(5):
                                alllist.append([i1+1,i2+1,i3+1,i4+1,i5+1,i6+1,i7+1,i8+1])

while(len(r)<8):
    r.append(9)

for i in range(len(alllist)):

    total = sum(alllist[i][:n])

    if( alllist[i][0] <= r[0] and
        alllist[i][1] <= r[1] and
        alllist[i][2] <= r[2] and
        alllist[i][3] <= r[3] and
        alllist[i][4] <= r[4] and
        alllist[i][5] <= r[5] and
        alllist[i][6] <= r[6] and
        alllist[i][7] <= r[7] and
        total % k == 0
    ):
        anslist.append(alllist[i][:n])

anslist = remove_repetition(anslist)

anslist = anslist[1:]

for i in anslist:
    print(" ".join(map(str, i)))