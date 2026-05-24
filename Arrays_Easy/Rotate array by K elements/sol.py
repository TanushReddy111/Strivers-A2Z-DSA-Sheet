arr = [ 1, 2, 3, 4, 5, 6]
k =2
def solve( arr, k):
    if k <=0:
        return
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i]= arr[ i+1]
    arr[len(arr)-1] = temp

    solve( arr, k-1)

solve(arr, k)

print( arr)