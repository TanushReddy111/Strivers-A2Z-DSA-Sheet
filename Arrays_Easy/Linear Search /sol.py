arr= [ 5, 4, 3, 2, 1]
num =5

def solve( arr, num):
    for index, i in enumerate(arr):
        if i == num:
            return index
    return -1

print( solve( arr, num))
    