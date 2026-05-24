arr =[ 1]

def find_small(arr: list):
    temp = float("inf")
    for i in arr:
        if i< temp:
            temp =i
    return temp

def find_large(arr):
    temp =  float("-inf")
    for i in arr:
        if i> temp:
            temp = i
    return temp

def solve(arr: list):
    if len(arr) < 2:
        return -1
    else:
        small = find_small(arr)
        arr.remove(small)
        large = find_large(arr)
        arr.remove(large)
        second_Small = find_small(arr)
        second_big = find_large(arr)
        while second_Small == small:
            arr.remove(second_Small)
            second_Small = find_small(arr)
        while second_big == large:
            arr.remove(second_big)
            second_big = find_large(arr)

        return second_Small,second_big
    
print( solve(arr))