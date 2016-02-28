#!/usr/bin/python3

import sort_utils as su

def _radix_sort_10(a, i):
    """
    Radix sort the array using the base 10 ** i
    """
    b = 10 ** i

    # A new array to hold values temporarily
    new = [[] for i in range(10)]

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
        r = q % 10

        new[r].append(n)

    # Flatten temporary array
    ret = [n for i in range(10) for n in new[i]]
    return ret, z < len(a)

def _radix_sort_16(a, i):
    """
    Radix sort the array using the base 16 ** i
    """
    b = 1 << (i << 2)

    # A new array to hold values temporarily
    new = [[] for i in range(16)]

    # Number of zero quotients. If the number of zero quotients equal to the
    # length of the array, that means we don't need to continue with radix sort.
    # I.e. no elements are higher than b
    z = 0
    for n in a:
        # Compute quotient and reminder for evey number, and store it in the
        # temporary array accordingly
        q = n >> (i << 2)
        if q == 0:
            z += 1
        r = q & 0xf

        new[r].append(n)

    # Flatten temporary array
    ret = [n for i in range(16) for n in new[i]]
    return ret, z < len(a)


def radix_sort(array, radix=16):
    i = 0
    cont = True
    if radix == 16:
        f = _radix_sort_16
    elif radix == 10:
        f = _radix_sort_10
    else:
        raise SortError("Unsupported radix")

    while cont:
        array, cont = _radix_sort_16(array, i)
        i += 1

    return array

if __name__ == "__main__":
    print("Sort with radix 16");
    su.test_sort(radix_sort, args=(16,))
    print("Sort with radix 10");
    su.test_sort(radix_sort, args=(10,))

# vim: set tw=80 sw=4:
