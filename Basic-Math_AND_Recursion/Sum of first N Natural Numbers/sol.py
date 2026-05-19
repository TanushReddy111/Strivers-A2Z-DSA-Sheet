num = int( input( "Enter Number:- "))
sol =0

def solve( num, sol):
    if 0 == num:
        return sol

    sol += num

    return solve( num -1, sol)

print( solve( num, sol))