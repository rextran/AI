import math
import time
def calc_mean(n):
	s = sum(n)
	N = len(n)
	mean = s/N
	return mean
def calc_median(n)
start = time.time()
donations = [100, 20.1, 39, 8, 12, 23, 12, 1020, 123, 291]
mean_Val = calc_mean(donations)
print("Trung binh", mean_Val)
print("Thoi gian", (time.time() - start)*1000)