p = {
	0:0,
	1:1,
	2:5,
	3:8,
	4:9,
	5:10,
	6:17,
	7:17,
	8:20,
	9:24,
	10:30
}

# p = {
# 	0:0,
# 	1:50,
# 	2:200,
# 	3:270
# }

max_n = 10

CUT_COST = 0

def cut_rod_recursive(p, n):
	if n == 0:
		return CUT_COST
	else:
		opt = 0
		for i in range(1, min(n, max_n) + 1):
			opt = max(opt, p[i] + cut_rod_recursive(p, n - i) - CUT_COST)
		return opt

memoization_table = {}
def cut_rod_memoization(p, n):
	if n == 0:
		return CUT_COST
	elif n in memoization_table:
		return memoization_table[n]
	else:
		opt = 0
		for i in range(1, min(n, max_n) + 1):
			opt = max(opt, p[i] + cut_rod_memoization(p, n - i) - CUT_COST)
		memoization_table[n] = opt
		return opt


def cut_rod_bottom_up(p, n):
	bottom_up_sols = [0]
	for i in range(1, n + 1):
		opt = 0
		for idx in range(max(0, i-10), i):
			sub_p = bottom_up_sols[idx]
			rest = p[i - idx]
			opt = max(opt, rest + sub_p)
		bottom_up_sols.append(opt)
	return bottom_up_sols[-1]




print(cut_rod_memoization(p, 450))





timing = False
if timing:
	import time
	for rod_size in range(3, 4):
		input_size = rod_size
		print(input_size)
		start = time.time()
		(cut_rod_recursive(p, rod_size))
		print("Time Elapsed Recursive: {}".format(time.time() - start))

		start = time.time()
		print(cut_rod_memoization(p, rod_size))
		print("Time Elapsed Memoization: {}".format(time.time() - start))

		start = time.time()
		print(cut_rod_bottom_up(p, rod_size))
		print("Time Elapsed Bottom Up: {}".format(time.time() - start))