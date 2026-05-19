
num = int( input( "Enter Number:- "))
num_copy = num
length = len(str(num))    

sol= 0

while num > 0:
    last_digt = num%10
    sol += last_digt ** length
    num = num//10

print (sol == num_copy)
