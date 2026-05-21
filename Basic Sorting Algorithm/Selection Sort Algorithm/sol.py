arr = [13,46,24,52,20,9]
N =6
 
def solve( arr, N):
    for i in range(N-1):
        min_index = i
        for j in range(i,N):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp1 = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp1
    return arr
 
print( solve( arr, N))
 