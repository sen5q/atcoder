a, b, k =map(int, input().split())

count = 0

while a < b:
    count += 1
    a = a*k

print( count )