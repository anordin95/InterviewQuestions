import math
INF = math.inf

p = [10, 100, 5, 50]
p = [30, 35, 15, 5, 10, 20, 25]

num_matrices = len(p) - 1
m = [[INF for _ in range(num_matrices)] for _ in range(num_matrices)]
n = [[INF for _ in range(num_matrices)] for _ in range(num_matrices)]

for i in range(num_matrices):
	m[i][i] = 0

# i = first index into m
# j = second index into m
def find_optimal_structure(i, j):
	if i == j:
		return 0
	elif m[i][j] != INF:
		return m[i][j]
	else:
		# opt = m[i][j]
		for k in range(i, j):
			cost = find_optimal_structure(i, k) + find_optimal_structure(k + 1, j) + p[i]*p[k+1]*p[j+1]
			if i == 2 and j == 5:
				print("i,k: {}; k+1,j: {}; pqr: {}".format(find_optimal_structure(i, k), find_optimal_structure(k + 1, j), p[i]*p[k+1]*p[j+1]))

				print("i: {}, j: {}, k: {}".format(i,j,k))
				print("cost: {}".format(cost))
			if cost < m[i][j]:
				m[i][j] = cost
				n[i][j] = k 
		# n[i][j] = best_k
		# m[i][j] = opt
		return cost

def find_optimal_solution(i, j):
	if i == j:
		print("A{}".format(i))
	else:
		print("(")
		find_optimal_solution(i, n[i][j])
		find_optimal_solution(n[i][j] + 1, j) 
		print(")")



find_optimal_structure(0, num_matrices-1)

# find_optimal_solution(0, num_matrices-1)
