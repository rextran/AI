import math
import time
from collections import Counter
def calc_mean(n):
	s = sum(n)
	N = len(n)
	mean = s/N
	return mean
def calc_median(n):
	N = len(n)
	print(N)
	n.sort()
	if(N%2 == 0):
		med = (n[int(N/2)] + n[int(N/2 -1)])/2.0
	else:
		med = n[int(N/2) - 1]
	return med

def calc_mode(n):
	c = Counter(n)
	print(c)
	mode = c.most_common(1)
	print(mode)
	return mode[0][0]
start = time.time()
donations = [100, 20.1, 39, 8, 12, 23, 12, 1020, 123, 291]
points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 6, 6, 1, 5, 6, 7, 8, 6, 1, 10]
mean_Val = calc_mean(donations)
meadian_Val = calc_median(donations)
mode_Val = calc_mode(points)
print("Trung binh", mean_Val)
print("Trung vi", meadian_Val)
print("Mode", mode_Val)
print("m", )
print("Thoi gian", (time.time() - start)*1000)