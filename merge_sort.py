#Merge_sort
import random

a = [1,2,3]
b = [3,2,1]
c = [random.randint(1,500) for _ in range(0, 100)]
d = []
e = [1]

def merge(arr1, arr2):
	n_1 = len(arr1)
	n_2 = len(arr2)
	idx_1 = 0
	idx_2 = 0
	merged_arr = []
	while idx_1 < n_1 and idx_2 < n_2:
		arr1_e = arr1[idx_1]
		arr2_e = arr2[idx_2]
		if arr2_e > arr1_e:
			merged_arr.append(arr1_e)
			idx_1 += 1
		else:
			merged_arr.append(arr2_e)
			idx_2 += 1
	if idx_1 < n_1:
		merged_arr += arr1[idx_1:]
	if idx_2 < n_2:
		merged_arr += arr2[idx_2:]
	return merged_arr

def merge_sort(arr):
	if len(arr) == 1 or len(arr) == 0:
		return arr
	
	middle = len(arr)//2
	first_half = arr[0: middle]
	second_half = arr[middle:]

	return merge(merge_sort(first_half), merge_sort(second_half))

def quick_sort(arr):
	less = []
	equal = []
	greater = []

	if len(arr) > 1:
		pivot = arr[0]
		for x in arr:
			if x < pivot:
				less.append(x)
			elif x == pivot:
				equal.append(x)
			elif x > pivot:
				greater.append(x)
		return quick_sort(less) + equal + quick_sort(greater)
	else:
		return arr

print(merge_sort(a))
print(merge_sort(b))
print(merge_sort(c))
print(merge_sort(d))
print(merge_sort(e))

print(quick_sort(a))
print(quick_sort(b))
print(quick_sort(c))
print(quick_sort(d))
print(quick_sort(e))

