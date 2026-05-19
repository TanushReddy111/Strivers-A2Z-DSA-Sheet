num = 5
arr = [5,4,3,2,1]
count = 0
def solve( num, arr: list, count):
    if 1 == num:
        return arr
    
    temp = arr[num]
    arr[num]= arr[count]
    arr[count] = temp

    return solve( num -1, arr, count +1)

print( solve( num -1, arr, count))

    
