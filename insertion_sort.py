#!/usr/bin/python3

import sort_utils as su

def insertion_sort(array, *, stride=1):
    """
    Perform insertion sort on 'array'. The 'stride' parameter is useful for
    shell sort
    """
    # Compare element at i with everthing behind it. When a lesser element is
    # found, we swap. Stop comparison when one's found. The slice [0:i] always
    # remain sorted. Insertion sort is a stable sort.
    #
    # It's as if an element at i is inserted into an already-sorted array
    # [0:i-1]. This could be performed using binary searching the array [0:i-1]
    # (as it's already sorted), but it'd involve pushing some elements to right.
    # We also need to factor in for duplicate elements
    n = len(array)
    i = 0
    while i < n:
        j = i
        while j >= stride and array[j - stride] > array[j]:
            su.xchg(array, j, j - stride)
            j -= stride
        i += 1

    return array

if __name__ == "__main__":
    su.test_sort(insertion_sort)

# vim: set tw=80 sw=4:
