arr = [ 1, 1, 0, 1, 1, 1]

def solve( arr):
    max =0

    for index,  i in enumerate(arr):
        if i ==1:
            temp =count1(arr, index)
            if temp > max:
                max = temp
    return max


def count1( arr, i):
    temp =0
    while i < len(arr) and arr[i] ==1:
        temp +=1
        i+=1 
    return temp

        


print( solve( arr))
        