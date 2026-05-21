arr = [5, 4, 4, 1, 1]
 
def solve( arr):
    n = len(arr)
 
    for i in range( 1, n):
        temp = arr[i] # Value to compare
        j = i-1  # previous num index
        
        while j>= 0 and arr[j]>temp:
            arr[j+1]= arr[j]
            j -= 1
        arr[j+1] = temp
    return arr
 
print( solve( arr))
 