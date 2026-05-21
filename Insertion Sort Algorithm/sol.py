arr = [ 1, 1, 4, 4, 5]
 
def solve( arr):
    for index, num in enumerate(arr):
        temp_num = num 
        index2 =index -1
        temp=0
        while index2>= 0 and arr[index2]> temp_num:
            arr[index-temp] = arr[ index2]
            index2 -=1
            temp +=1
        arr[index2+1] = temp_num
 
    return arr
 
print( solve( arr))