# TO-DO: Implement a recursive implementation of binary search

"""
define smallest value
define largest value
define mid value (smallest + largest / 2)
compare mid value w/ target value)
if mid value is not target value
    if mid value is smaller than target value re-define upper bound to mid value
    if mid value is larger than target value re-define lower bound to mid value
"""


def binary_search(arr, target, start, end):
    start = 0
    end = len(arr) - 1

    if len(arr) == 0:
        return -1

    while start <= end:
        mid = start + end // 2

        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
    return False


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
