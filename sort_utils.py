
from random import randint

def print_array(p, a):
    """
    Print the array 'a' with message 'p'
    """
    print("{:>10s}:".format(p), end=' ')
    for i in a:
        print("{:>3d}".format(i), end=' ')
    print()


def check_array(a):
    """
    Check the array 'a' is sorted
    """
    print_array("FINAL", a)
    i = 0
    while i < (len(a) - 1):
        if a[i + 1] < a[i]:
            print("Sort error at index {:d}".format(i + 1))
            return
        i += 1


def print_index(n):
    """
    Print a line of 'n' array indices
    """
    print_array("INDEX", (i for i in range(n)))


def get_array(n, r=99):
    """
    Get an array of size n with random integers
    """
    return [randint(0, r) for i in range(n)]


def get_unique_array(n, r=99):
    """
    Get an array of size n with random but unique integers
    """
    a = []
    i = 0
    while i < n:
        while True:
            x = randint(0, r)
            if x not in a:
                a.append(x)
                break
        i += 1
    return a

def xchg(a, i, j):
    """
    Exchange elements at 'i' and 'j' in array 'a'
    """
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

class SortError(Exception):
    pass

# vim: set tw=80 sw=4:
