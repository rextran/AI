import math
def giaiThua(n):
	if(n == 0 or n == 1):
		return 1
	else:
		return n*giaiThua(n-1)

print(giaiThua(5))

N = 100
e = 0
for i in range(N):
	e = e + 1/giaiThua(i)

print(e)