arr = [ 2,2,1]

def solve( arr):
    dictionary= {}
    
    for i in arr:
        dictionary[i] = dictionary.get(i,0)+1
    
    for key in dictionary:
        if dictionary[key]==1:
            return key
    return -1

print( solve( arr))