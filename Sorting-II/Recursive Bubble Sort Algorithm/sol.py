arr = [ 13, 46, 24, 52, 20, 9]
n = len(arr)
def buble_sort( arr, n):
    if n ==1:
        return
    did_swap = False
    for i in range(n-1):
        if arr[i]> arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            did_swap = True
    
    # Condition to make the solution more efficient.
    if True== did_swap:
        return 
    
    buble_sort( arr, n-1)

buble_sort(arr, n)

print (arr)