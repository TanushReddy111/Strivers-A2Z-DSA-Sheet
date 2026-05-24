arr =[ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]

def solve( arr: list):
    j =0

    for i in range(0, len(arr)):
        if arr[i]!= 0:
            arr[j], arr[i]= arr[i], arr[j]
            j += 1
    return arr

print(solve(arr))