#!/usr/bin/python3

import sort_utils as su

def bubble_sort(array):
    """
    Perform bubble sort on 'array'
    """
    # Compare element at j to the one immediately follows, and perform this for
    # all elements in the array. When a number less than j is found, we swap.
    # Stop sorting when there were no swaps were made in the inner loop
    n = len(array)
    i = 0
    while i < (n - 1):
        j = 0
        done_xchg = False
        while j < (n - 1):
            if array[j + 1] < array[j]:
                su.xchg(array, j, j + 1)
                done_xchg = True
            j += 1
        if not done_xchg:
            break
        i += 1

    return array


if __name__ == "__main__":
    su.test_sort(bubble_sort)

# vim: set tw=80 sw=4:
