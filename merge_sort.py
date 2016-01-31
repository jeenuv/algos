#!/usr/bin/python3

import sort_utils as su

N = 10
array = su.get_array(N)
su.print_index(N)
su.print_array("start", array)

def merge_sort(a):
    assert len(a) >= 2
    if len(a) == 2:
        # List has two elements. Simple sort a copy and return it
        if a[0] > a[1]:
            tmp = a[:]
            su.xchg(tmp, 0, 1)
            return tmp
        else:
            return a
    else:
        # List has more than two elements. Split a copy of the list into two,
        # and apply merge sort separately to two lists. Then merge them into one
        l0 = len(a) // 2
        l1 = len(a) - l0

        # Call merge sort recursively only if the sub-lists themselves contain
        # than 2. Otherwise, they're sorted already, and we can avoid a function
        # call
        a0 = merge_sort(a[:l0]) if l0 >= 2 else a[:l0]
        a1 = merge_sort(a[l0:]) if l1 >= 2 else a[l0:]

        # Merge sub-arrays into one
        i0, i1 = 0, 0
        m = []

        # Iterate individual arrays, and copy the smallest into a final one,
        # until we exchaust either one
        while i0 < l0 and i1 < l1:
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


m = merge_sort(array)
su.check_array(m)

# vim: set tw=80 sw=4:
