from collections import defaultdict
arr = [2,2,3,4,4,2]
 
def solve( arr):
 
    dictionary = defaultdict(int)
 
    for index, element in enumerate(arr):
 
        dictionary[element] += 1
    return dictionary
 
 
high = 0
low = float('inf')
high_element =  None
low_element = None
 
dictionary = solve( arr)
for index, element in enumerate(dictionary):
 
        if high < dictionary[element]:
            high = dictionary[element]
            high_element = element
        if low > dictionary[element]:
            low = dictionary[element]
            low_element = element
 
print( high_element, low_element)
 
 