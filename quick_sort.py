#!/usr/bin/python3

import sort_utils as su

def quick_sort(array):
    """
    Perform quick sort with 3-way partitioning on 'array'
    """
    def do_sort(lo, hi):
        if lo >= hi:
            return

        # Elements below lt are less than p; elements above gt are greather than
        # p; elements between lt and i are equal to p
        p = array[lo]
        lt, gt = lo, hi
        i = lo

        while i <= gt:
            if array[i] < p:
                su.xchg(array, i, lt)
                i += 1
                lt += 1
            elif array[i] > p:
                su.xchg(array, i, gt)
                gt -= 1
            else:
                i+= 1

        do_sort(lo, lt - 1)
        do_sort(lt + 1, hi)

    do_sort(0, len(array) - 1)
    return array

if __name__ == "__main__":
    su.test_sort(quick_sort);

# vim: set tw=80 sw=4:
