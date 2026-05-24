arr = [ -1, 0, 3, 6]

def solve( arr: list):
    temp = arr[0]
    arr.remove(temp)
    arr.append(temp)
    return arr

print( solve( arr))