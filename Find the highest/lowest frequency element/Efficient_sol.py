arr = [10,5,10,15,10,5]

def solve( arr):
    dictionary = {}
    for number in arr: 
        dictionary[number] = dictionary.get(number, 0)+1
    return dictionary

print( solve(arr))

# min, max TO Do ...