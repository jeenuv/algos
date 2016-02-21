#!/usr/bin/python3

import sort_utils as su

def heap_sort(array):
    """
    Perform heap sort on 'array'
    """
    # Array representation of a heap (almost-complete binary tree): an element
    # will be at index i; its immediate left child will be at i+1, and right
    # child at i+2. Root will be at index 0.
    left = lambda i: (2 * i) + 1
    right = lambda i: left(i) + 1

    def heapify(n, i):
        """
        Make sure the element at 'i' is smaller than its children. If it isn't, then
        swap with the smaller among its children. Then heapfiy on the swapped child
        """
        l, r = left(i), right(i)

        # Find the smallest among the node and its children
        smallest = i
        if l >= n:
            # If there's no left child, there can't be a right child either
            # (almost-complete binary tree)
            return
        elif array[l] < array[i]:
            smallest = l
        if r < n and array[r] < array[smallest]:
            smallest = r
        if smallest != i:
            su.xchg(array, i, smallest)
            heapify(n, smallest)

    # For an array containing n elements, those at indices from and including n//2
    # onwards are leaves. The one at ((n//2) - 1) is the last non-leaf in the
    # almost-complete binary tree, and that's where we start the heapify operation.
    #
    # For every non-leaf node (from the farthest to the root), do heapify. At the
    # end of this iteration, the smallest would have found its way up to the root.
    # Extract the root, replace it with the last leaf, and repeat the process again,
    # only this time with the length of the heap reduced
    n = len(array)
    final = []
    while n > 0:
        i = (n // 2) - 1
        while i >= 0:
            heapify(n, i)
            i -= 1
        final.append(array[0])
        array[0] = array[n-1]
        n -= 1

    return final

if __name__ == "__main__":
    N = 10
    array = su.get_array(N)
    su.print_index(N)
    su.print_array("start", array)
    array = heap_sort(array)
    su.check_array(array)

# vim: set tw=80 sw=4:
