from collections import defaultdict

arr = [10,5,10,15,10,5]


def solve( arr):
    dictionary = defaultdict(int)
    for element in arr:
        dictionary[element]+=1

    for key, value in dictionary.items():
        print( key, value)

solve( arr)