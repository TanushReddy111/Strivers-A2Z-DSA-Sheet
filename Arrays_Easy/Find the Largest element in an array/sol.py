arr =[ 8, 10, 5, 7, 9]

temp = float("-inf")

for i in arr:
    if i> temp:
        temp = i

print(temp)