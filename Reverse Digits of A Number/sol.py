num = int(input("Enter number:- "))

finalNum =0

while num >0:

    lastdigit = num%10
    finalNum = finalNum*10 + lastdigit
    num = num // 10

print("reversed number is:- ", finalNum)