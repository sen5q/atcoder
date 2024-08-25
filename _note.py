#文字
#整数
#小数

#1個　
input()
int(input())
float(input())

#1行複数
input().split()
map(int, input().split())
map(float, input().split())

#1行の配列
input().split()
list(map(int, input().split()))
list(map(float, input().split()))

#複数行配列
[input().split() for _ in range(n)]
[list(map(int, input().split())) for _ in range(n)]
[list(map(float, input().split())) for _ in range(n)]
