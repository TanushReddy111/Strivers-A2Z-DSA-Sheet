arr= [ 3,2,8,5,1,4,23]
low = 0
high = len(arr) -1
 
def merge(arr, low, mid, high):
    # two arrays:- 
    # low - mid
    # mid+1 = high
    first = low
    second = mid+1
    temp = []
    while first <=mid and second <=high:
        if (arr[first]< arr[second]):
             temp.append(arr[first])
             first +=1
        else:
            temp.append(arr[second])
            second +=1
    while first > mid and second <=high:
        temp.append(arr[second])
        second +=1
    while first<= mid and second > high:
        temp.append(arr[first])
        first +=1
    
    for i in range(len(temp)):
        arr[low+i] = temp[i]
 
 
def merge_sort( arr, low, high):
    if low >= high:
        return low, high
    mid = (low+ high)//2
 
    merge_sort( arr, low, mid)  
    merge_sort( arr, mid+1, high)  
 
    merge( arr,low, mid, high)
 
merge_sort( arr, low, high)
print( arr)