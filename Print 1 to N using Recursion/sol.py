num = int( input( "Enter number:- "))
sol = []
count = 1
def print_num( num, sol: list, count):
    if count > num:
        return sol 
    sol.append(count)
    return print_num( num, sol, count +1 )

print( print_num( num, sol, count))