num = int( input( " Enter Number:- "))
sol = []

def print_number( num, sol: list):
    if 0 == num:
        return sol
    
    sol.append(num)
    
    return print_number( num-1, sol)


print( print_number( num, sol))
