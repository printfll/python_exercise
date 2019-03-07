import sys
def find_x(fn, y):
    i, j = 0, sys.maxsize
    while i<=j:
        mid = j-(j-i)/2
        res = fn(mid)
        if res == y:
            return mid
        if res < y:
            i = mid+1
        else:
            j = mid-1
    return -1