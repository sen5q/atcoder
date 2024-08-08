#文字
#整数
#小数

# 1行1列
s = input()
n = int(input())
f = float(input())

# 1行複数列
a, b = input().split()
n, y, z = map(int, input().split())
h, m, s = map(float, input().split())

# 1行配列
a = input().split()
a = list(map(int, input().split()))
a = list(map(float, input().split()))

#複数行配列
a = [input().split() for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
a = [list(map(float, input().split())) for _ in range(n)]