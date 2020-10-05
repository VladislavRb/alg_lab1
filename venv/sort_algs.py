def is_sorted(arr: list):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False

    return True


# лучший случай: n + 1 + n(1 + 2 + 3 + 1 + 1 + 3 + 3 + 1) = n + 1 + 15n = 1 + 16n
# худший случай: n + 1 + n(1 + 2 + 3 + 2 + n) + n(n - 1)/2 = n + 1 + 8n + n^2 + (n^2 - n) / 2 = 3n^2/2 + 17n/2 + 1

def insertion_sort(arr: list, k=0):
    n = len(arr) # n + 1

    for i in range(1, n): # 1 + 2
        if arr[i] <= arr[0]: # 3
            swapped_elem = arr[i] # 2
            del arr[i] # n - i + 1
            arr.insert(0, swapped_elem) # n
        else:
            for j in range(i - 1, -1, -1): # 1 + 1 + 2
                if arr[i] > arr[j]: # 3
                    if not j == i - 1: # 3
                        swapped_elem = arr[i] # 2
                        del arr[i] # n - i + 1
                        arr.insert(j + 1, swapped_elem) # n - j

                    break # 1


def quick_sort(arr: list, k: int, start_index=0, end_index=0):
    if not end_index:
        end_index = len(arr) - 1

    if end_index - start_index < k:
        arr_part = arr[start_index:(end_index + 1)]
        insertion_sort(arr_part)
        arr[start_index:(end_index + 1)] = arr_part

    else:
        sep_element = arr[end_index]
        sep_index = end_index

        for i in range(end_index - 1, start_index - 1, -1):
            if arr[i] > sep_element:
                arr.insert(sep_index + 1, arr[i])
                del arr[i]
                sep_index -= 1

        if sep_index - start_index > 1:
            quick_sort(arr, k, start_index, sep_index - 1)

        if end_index - sep_index > 1:
            quick_sort(arr, k, sep_index + 1, end_index)


def merge_arrays(first_half: list, second_half: list):
    sorted_arr = []
    first_index = 0
    second_index = 0

    while True:
        if first_half[first_index] < second_half[second_index]:
            sorted_arr.append(first_half[first_index])
            first_index += 1
        else:
            sorted_arr.append(second_half[second_index])
            second_index += 1

        if first_index == len(first_half):
            sorted_arr.extend(second_half[second_index:])
            break

        if second_index == len(second_half):
            sorted_arr.extend(first_half[first_index:])
            break

    return sorted_arr


def merge_sort(arr: list, k: int):
    if len(arr) > k:
        sep_index = int(len(arr) / 2)
        first_half = arr[:sep_index]
        second_half = arr[sep_index:]

        merge_sort(first_half, k)
        merge_sort(second_half, k)

        arr[:] = merge_arrays(first_half, second_half)
    else:
        insertion_sort(arr)
