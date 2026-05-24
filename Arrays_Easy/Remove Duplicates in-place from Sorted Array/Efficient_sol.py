arr = [ 1,1,1,2,2,3,3,3,3,4,4]

def solve( arr: list):
    j =0
    for i in range(1, len(arr)-1):
        if arr[j] != arr[i]:
            j+=1
            arr[j] = arr[i]
    return arr[:j+1]
print( solve( arr))