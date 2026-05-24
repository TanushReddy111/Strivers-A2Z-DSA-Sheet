arr = [ 1,2,3,4,5]

def is_ascending(arr):
    for i in range(0,len(arr)-2):

        if arr[i]> arr[i+1]:
            return False
    return True

def is_decending(arr):
    for i in range(0, len(arr)-2):
        if arr[i]< arr[i+1]:
            return False
    return True
    
def solve( arr):
    if is_ascending(arr) or is_decending(arr):
        return True
    return False

print( solve( arr))