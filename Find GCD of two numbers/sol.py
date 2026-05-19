num1 = int(input("Enter number 1:- "))

num2 = int( input("Enter number 2:- "))

if num1<num2:
    num =num1
else:
    num= num2

while num>0:
    if (num1%num ==0 and num2%num==0):
        break
    else:
        num -=1
if 0==num:
    print("No common factor ")
else:
    print("Greatest common factor:- ", num)