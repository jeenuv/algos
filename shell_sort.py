#!/usr/bin/python3

import sort_utils as su
from insertion_sort import insertion_sort

def shell_sort(array):
    def find_h(n):
        """
        For a given 'n', find an largest h such that (3*h + 1) < n
        """
        h = 0
        while h < n:
            t = h
            h = (3 * t) + 1
        return t

    # Shell sort is repeated insertion sort, but peformed with decreasing values
    # of stride, h. We first start with the largest h that's less that the total
    # number of elements. The repeat the sort with h/3 and so on
    n = len(array)
    h = find_h(n)
    while h > 0:
        array = insertion_sort(array, stride=h)
        h = h // 3

    return array

if __name__ == "__main__":
    N = 20
    array = su.get_array(N)
    su.print_index(N)
    su.print_array("start", array)
    array = shell_sort(array)
    su.check_array(array)

# vim: set tw=80 sw=4:
