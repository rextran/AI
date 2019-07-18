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
	mode = c.most_common()
	max_val = mode[0][1]
	result = [mode[0][0]]
	for i in range(1, len(mode) -1):
		if(max_val == mode[i][1]):
			result.append(mode[i][0])
	return result

def frequency_table(n):
	table = Counter(n)
	numbers_freq = table.most_common()
	numbers_freq.sort()
	print("Number\tFrequency")
	for i in numbers_freq:
		print('{0}\t\t{1}'.format(i[0], i[1]))

def rangeOfData(n):
	lowest = min(n)
	highest = max(n)
	ran = highest - lowest
	print('Lowest: {0}\tHighest: {1}\tRange: {2}'.format(lowest, highest, ran))

def calc_variance(n):
	mean = calc_mean(n)
	N = len(n)
	diff = []
	for num in n:
		diff.append(num - mean)
	square_diff = []
	for d in diff:
		square_diff.append(d**2)
		sum_square_diff = sum(square_diff)
		variance = sum_square_diff/N
	return variance
start = time.time()
donations = [100, 20.1, 39, 8, 12, 23, 12, 1020, 123, 291]
points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 6, 6, 1, 5, 6, 7, 8, 6, 1, 10]
mean_Val = calc_mean(donations)
meadian_Val = calc_median(donations)
mode_Val = calc_mode(points)
print("Trung binh", mean_Val)
print("Trung vi", meadian_Val)
print("Mode", mode_Val)
print(frequency_table(points))
rangeOfData(points)
print("Variance", calc_variance(points))
print("Standard Deviation", calc_variance(points)**0.5)
print("Thoi gian", (time.time() - start)*1000)