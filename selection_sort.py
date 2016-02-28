#!/usr/bin/python3

import sort_utils as su

def selection_sort(array):
    # Compare element at i with everything to its right. When a number less than
    # i is found, we swap. The slice [0:i] always remain sorted. Stop sorting
    # when there were no swaps made
    n = len(array)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if array[j] < array[i]:
                su.xchg(array, i, j)
            j += 1
        i += 1

    return array

if __name__ == "__main__":
    su.test_sort(selection_sort)

# vim: set tw=80 sw=4:
