#Note:- This is a recursive SHIFT based insertion approach
arr = [ 5,4,3,2,1]
 
 
def solve( arr, p1):
    if p1 >= len(arr):
        return
    temp = arr[p1]
 
    i = p1-1
    j=0
    while i >=0 and arr[i]>temp:
        arr[p1-j] = arr[i]
        j += 1
        i -=1
        
    arr[i+1] = temp
 
    
    solve( arr, p1+1)
    
solve( arr, 1)
 
print( arr)