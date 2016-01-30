#!/usr/bin/python3

import sort_utils as su

N = 10
array = su.get_array(N)
su.print_index(N)
su.print_array("start", array)

# Compare element at j to the one immediately follows, and perform this for all
# elements in the array. When a number less than j is found, we swap. Stop
# sorting when there were no swaps were made in the inner loop
i = 0
while i < (N - 1):
    j = 0
    done_xchg = False
    while j < (N - 1):
        if array[j + 1] < array[j]:
            su.xchg(array, j, j + 1)
            done_xchg = True
        j += 1
    if not done_xchg:
        break
    i += 1

su.check_array(array)

# vim: set tw=80 sw=4:
