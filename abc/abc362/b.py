import math
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

ab = math.sqrt( (ax-bx)**2 + (ay-by)**2 )
ac = math.sqrt( (ax-cx)**2 + (ay-cy)**2 )
bc = math.sqrt( (bx-cx)**2 + (by-cy)**2 )

if   math.isclose( (ab**2 + bc**2), ac**2 ):
  print("Yes") 
elif math.isclose( (ab**2 + ac**2), bc**2 ):
  print("Yes") 
elif math.isclose( (bc**2 + ac**2), ab**2 ):
  print("Yes") 
else:
  print("No")
