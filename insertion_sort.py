#!/usr/bin/python3

import sort_utils as su

N = 10
array = su.get_array(N)
su.print_index(N)
su.print_array("start", array)

# Compare element at i with everthing behind it. When a lesser element is found,
# we swap. Stop comparison when one's found. The slice [0:i] always remain
# sorted
#
# It's as if an element at i is inserted into an already-sorted array [0:i-1].
# This could also be performed using binary searching the array [0:i-1] (as it's
# already sorted, but it'd involve pushing some elements to right. But we need
# to factor in for duplicate elements
i = 0
while i < N:
    j = i
    while j > 0 and array[j - 1] > array[j]:
        su.xchg(array, j, j - 1)
        j -= 1
    i += 1

su.check_array(array)

# vim: set tw=80 sw=4:
