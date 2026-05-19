num = int(input("Enter Number:- "))
temp = num
finalNum =0

while num>0:
    lastdigit= num%10
    num = num //10
    finalNum = finalNum * 10 + lastdigit

if(temp == finalNum):
    print( "It is a Palindrome")
else:
    print("It is not a palindrome")
    