#!/usr/bin/python3

import sort_utils as su

def insertion_sort(h):
    """
    Perform ordinary insertion sort, but start at h. Perform comparisons with
    previous elements with stride stride 'h'
    """
    i = h
    while i < N:
        j = i
        while j >= h and array[j - h] > array[j]:
            su.xchg(array, j - h, j)
            j -= h
        i += 1
    su.print_array("{:d}-sort".format(h), array)

def find_h(n):
    """
    For a given 'n', find an largest h such that (3*h + 1) < n
    """
    h = 0
    while h < n:
        t = h
        h = (3 * t) + 1
    return t

N = 20
array = su.get_array(N)
su.print_index(N)
su.print_array("start", array)

# Shell sort is repeated insertion sort, but peformed with decreasing values of
# stride, h. We first start with the largest h that's less that the total number
# of elements. The repeat the sort with h/3 and so on
h = find_h(N)
while h > 0:
    insertion_sort(h)
    h = h // 3

su.check_array(array)

# vim: set tw=80 sw=4:
