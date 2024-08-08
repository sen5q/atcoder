import math

a, b, d = map(int, input().split())

d0 = math.atan2(b, a)

r = math.sqrt((a*a) + (b*b))


d1 = d0 + math.radians(d)

dx = r * math.cos(d1)
dy = r * math.sin(d1)

print(dx, dy)