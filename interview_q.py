arr1 = [1, 3, 1, 2]  # False
arr2 = [1, 1, 1, 1]  # True


def has_complete_cycle(array):
    n = len(array)
    idx = 0
    num_visited = 0
    a = list(range(0, n))

    while idx < n:
        a[idx] = -1
        idx += array[idx]
        num_visited += 1

    all_visited = True
    for item in a:
        if item != -1:
            all_visited = False

    print(all_visited)
    print(num_visited)
    print(idx % n)

    return (all_visited) and (num_visited == n) and (idx % n == 0)


print(has_complete_cycle(arr1))
print(has_complete_cycle(arr2))
