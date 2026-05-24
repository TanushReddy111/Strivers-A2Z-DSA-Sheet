arr1 = [ 1,2,3,4,5,6,7,8,9,10]

arr2 = [ 2,3,4,4,5,11,12]

def solve( arr1, arr2):
    temp = []
    for i in arr1:
        temp.append(i)
    for i in arr2:
        temp.append(i)
    return list(set(temp))
    
print( solve(arr1, arr2))