import math
ans = 0
default = 100
ans = math.sqrt(default)
A = []
for i in range ( 1 , 98 ,1):
    A.append( 100 - i )
for i in A:
    ans = math.sqrt(ans * ( i - 1 ) + 1 )
print(ans)