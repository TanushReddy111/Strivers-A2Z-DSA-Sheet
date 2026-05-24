arr = [4,1,7,9,3]
low =0
high = len(arr)-1
def partition( arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1



def solve (arr, low, high):
    
    if low< high:
        pivot_index= partition(arr, low, high)

        solve(arr, low, pivot_index-1)
        solve( arr, pivot_index+1, high)

solve(arr, low, high)

print( arr)