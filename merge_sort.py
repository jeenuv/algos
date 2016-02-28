#!/usr/bin/python3

import sort_utils as su

def merge_sort(array):
    """
    Perform merge sort on 'array'
    """
    # Recursively split the array into halves, sort, and merge the halves. Merge
    # sort is a stable sort (provided merge operation is stable)
    if len(array) <= 1:
        return array
    if len(array) == 2:
        # List has two elements. Simple sort a copy and return it
        if array[0] > array[1]:
            tmp = array[:]
            su.xchg(tmp, 0, 1)
            return tmp
        else:
            return array
    else:
        # List has more than two elements. Split a copy of the list into two,
        # and apply merge sort separately to two lists. Then merge them into one
        l0 = len(array) // 2

        # Call merge sort recursively on both halves
        a0 = merge_sort(array[:l0])
        a1 = merge_sort(array[l0:])

        # Merge sub-arrays into one
        i0, i1 = 0, 0
        m = []

        # Iterate individual arrays, and copy the smallest into a final one,
        # until we exchaust either one
        while i0 < len(a0) and i1 < len(a1):
            if a0[i0] < a1[i1]:
                m.append(a0[i0])
                i0 += 1
            elif a1[i1] < a0[i0]:
                m.append(a1[i1])
                i1 += 1
            else:
                m.append(a0[i0])
                m.append(a1[i1])
                i0 += 1
                i1 += 1

        # Copy any leftovers over
        m.extend(a0[i0:])
        m.extend(a1[i1:])

        return m

if __name__ == "__main__":
    su.test_sort(merge_sort)

# vim: set tw=80 sw=4:
