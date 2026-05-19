import math
num = int(input("Enter number:- "))
count =0

# while num>0:   #1
#     num = num//10    #num =1
#     count = count+1    #count=1

# print(f"the number has {count} digits")

print(int(math.log10(abs(num))+1))