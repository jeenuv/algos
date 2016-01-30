#!/usr/bin/python3

import sort_utils as su

N = 10
array = su.get_array(N)
su.print_index(N)
su.print_array("start", array)

# Compare element at i with everything to its right. When a number less than i
# is found, we swap. The slice [0:i] always remain sorted. Stop sorting when
# there were no swaps made
i = 0
while i < N:
    j = i + 1
    while j < N:
        if array[j] < array[i]:
            su.xchg(array, i, j)
        j += 1
    i += 1

su.check_array(array)

# vim: set tw=80 sw=4:
