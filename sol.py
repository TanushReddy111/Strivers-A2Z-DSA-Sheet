arr = [ -3, 2, 1]
k = 6

def solve( arr, k):
    temp =0
    final= 0
    for i in range( len( arr)):
        for j in range(i+1, len(arr)):
            
            if sum( arr[i:j])==k:
                temp =len( arr[i:j])
        if temp> final:
            final = temp
            
    return final

print( solve( arr, k))