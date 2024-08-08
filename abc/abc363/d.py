import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import math
n = int(input())

#1桁なら10個 0,1,2,3,4,5,6,7,8,9                  10個
#2桁なら9個  11,22,33,...,88,99                    9個
#3桁なら    1x1,2x2,3x3,...,8x8,9x9                 → 9*[  1桁の回文数個]
#4桁なら    1[00, 2桁の回文数]1,...,9[2桁の回文数]9 → 9*[  2桁の回文数個+1]
#5桁なら    1[3桁の回文数]1,...,9[3桁の回文数]9     → 9*[  3桁の回文数個+1]
#n桁なら    9 * [[(n-2)桁の回文数個]個] max35桁     → 9*[n-2桁の回文数個+1]

#3桁の1番目は101
#3桁の2番目は111
#3桁の3番目は121
#3桁の37番目は363 //46番目  3桁のは81個=9*ある

palind = [10,9,90]
digit = 0
sum = 19

for i in range(36):
    digit = i+1

    if(digit>=4):
        palind.append(  9 * (palind[digit-3] + 1 )  )

#print(palind)

n0 = n
for i in range(36):
    n -= palind[i]
    if n<=0:
        n += palind[i]  #戻して
        ans_digit = (i+1)   #桁数
        ans_banme = n
        break

#print( ans_digit, ans_banme )

ans_banme += 9
ans_banme = str(ans_banme)
ans_half  = str(ans_banme) 

ans = ans_banme 
if (ans_digit%2 == 1):
    ans = ans[:-1]


ans += ans_half[::-1]

print(ans)

