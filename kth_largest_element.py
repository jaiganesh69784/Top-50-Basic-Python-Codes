import heapq

def find_kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]
