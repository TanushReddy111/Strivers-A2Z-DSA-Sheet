arr = [1,2,3,4,6,7,8,9]

def solve( arr):
    length = len(arr)+1
    total = sum(arr)

    expected_total = length* (length+1)//2

    return expected_total - total

print( solve( arr))
    