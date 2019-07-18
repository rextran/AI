import random
import math
N = 100000 
# Số điểm sinh ra
N_T = 0
# Đếm số điểm trong đường tròn

for i in range(N): # Sinh các số nằm trong [-1, 1]
	x = random.random()*2 - 1 # random.random() sinh ra các số nằm trong đoạn [0, 1]
	y = random.random()*2 - 1

	x2 = x**2
	y2 = y**2

	if(math.sqrt(x2 + y2) <= 1.0):
		N_T += 1

pi = (N_T/N)*4
print(pi) 
print(math.exp(2))