arr = [ 5,4,3,2,1]
N = 5

def solve( arr, N):
    j =1
    while j< N:
        for i in range(N-1): 
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        j += 1
    return arr

print (solve( arr, N))