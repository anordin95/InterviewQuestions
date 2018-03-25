d = [1, 2, 3]

def is_zero(amt, denoms):
	if amt == 0:
		return 1
	elif amt < 0:
		return 0
	else:
		tot = 0
		for coin in denoms:
			t = is_zero(amt - coin, denoms)
			tot += t

		return tot

print(is_zero(4, d))

# def n_a(a):
# 	a.append(5)
# 	return a

# print(n_a([]))