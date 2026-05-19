num = int( input( "Enter number:- "))
sol = 1

def solve( num, sol):
    if 0 == num:
        return sol
    
    sol *= num
    
    return solve( num -1, sol)

print( solve( num, sol))