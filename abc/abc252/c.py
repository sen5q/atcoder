n = int(input())
s = [input().split() for _ in range(n)]

slotflag = list(range(n))
for i in range(n):
    slotflag[i] = 0


max = 0
time = 0

for target in range(10):

    time = -1

    #timer[target]
    while 1:
        time += 1
        tm = time%10

        for i in range(n):

            strslot = str(s[i])
            print(strslot[tm])
            if(strslot[tm] == str(target)):
                slotflag[i] = 1
                break
        
        stop = 1
        for i in range(n):
            if(slotflag[i] == 0):
                stop = 0
                break

        if(stop==1):
            break

    #time[target] compe
    if(max < time):
        max = time


print(time)