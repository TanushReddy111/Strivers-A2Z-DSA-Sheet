arr = [-3, 2, 1]
k = 0

def solve( arr, k):
    max = 0
    for i in range(len(arr)):
        
        for j in range(i, len(arr)):
            s  = sum(arr[i:j])
            if s == k and len(arr[i:j])> max:
                max = len(arr[i:j])
    return max
    
print( solve( arr, k))