import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------

import numpy as np

s = [input() for _ in range(8)]

#仮盤面を作成　0を「置けるマス」と定義
s2 = np.zeros((8,8))

for i in range(8):              #全てのマスについて
    for j in range(8):

        if s[i][j] == "#":      #ルークが置かれているなら

            for k in range(8):
                s2[i][k] = 1    #ヨコ一直線は置けないマスにする
                s2[k][j] = 1    #タテ一直線も置けないマスにする

#盤面のマス数から置けないマス数を引いたら答え
#0と1を逆にしといてcount_nonzeroするほうが楽
print( np.size(s2) - np.count_nonzero(s2) )