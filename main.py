from sort_algs import *
from random import randint
from time import time


def time_expenses_for(sort_method, n: int, m: int, p: int, k: int):
    sum_time = 0

    for j in range(m):
        array = [randint(0, p) for i in range(n)]

        start_time = time()
        sort_method(array, k)
        sum_time += time() - start_time

    return sum_time


n = 10000
m = 100
p = 10000

min_k_for_quick_sort = 2
min_k_for_merge_sort = 2

min_time_expenses_for_quick_sort = time_expenses_for(quick_sort, n, m, p, 2)
min_time_expenses_for_merge_sort = time_expenses_for(merge_sort, n, m, p, 2)

for k in range(3, 20):
    time_expenses_for_quick_sort = time_expenses_for(quick_sort, n, m, p, k)
    time_expenses_for_merge_sort = time_expenses_for(merge_sort, n, m, p, k)

    print("k =", k, ", quick sort:", time_expenses_for_quick_sort, ", merge sort:", time_expenses_for_merge_sort)

    if time_expenses_for_quick_sort < min_time_expenses_for_quick_sort:
        min_time_expenses_for_quick_sort = time_expenses_for_quick_sort
        min_k_for_quick_sort = k

    if time_expenses_for_merge_sort < min_time_expenses_for_merge_sort:
        min_time_expenses_for_merge_sort = time_expenses_for_merge_sort
        min_k_for_merge_sort = k

print("optimal k for quick sort:", min_k_for_quick_sort)
print("time expenses:", min_time_expenses_for_quick_sort)

print("optimal k for merge sort:", min_k_for_merge_sort)
print("time expenses:", min_time_expenses_for_merge_sort)
