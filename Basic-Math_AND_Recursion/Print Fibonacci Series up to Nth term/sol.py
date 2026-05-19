num = int( input( "Enter a number:- "))

prev = 0
curr = 1

def solve( prev, curr, num):
    if num <0:
        return print("")
    
    print( prev, end= " ")

    return solve( curr, curr+ prev, num -1)

solve( prev, curr, num)