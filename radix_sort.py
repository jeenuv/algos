#!/usr/bin/python3

import sort_utils as su

# Radix
R = 10

N = 10
array = su.get_array(N, 999)
su.print_index(N)
su.print_array("start", array)

def radix_sort(a, i):
    """
    Radix sort the array using the base R ** i
    """
    b = R ** i

    # A new array to hold values temporarily
    new = [[] for i in range(R)]

    # Number of zero quotients. If the number of zero quotients equal to the
    # length of the array, that means we don't need to continue with radix sort.
    # I.e. no elements are higher than b
    z = 0
    for n in a:
        # Compute quotient and reminder for evey number, and store it in the
        # temporary array accordingly
        q = n // b
        if q == 0:
            z += 1
        r = q % R

        new[r].append(n)

    # Flatten temporary array
    ret = [n for i in range(R) for n in new[i]]
    return ret, z < len(a)


i = 0
cont = True
while cont:
    array, cont = radix_sort(array, i)
    i += 1

su.check_array(array)
