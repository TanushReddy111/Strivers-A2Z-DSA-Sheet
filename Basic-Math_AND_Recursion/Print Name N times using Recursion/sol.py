num =int( input( "Enter number:- "))
name = str( input( "Enter your name:- "))
sol =""

def print_name( num, sol: str, name):
    if( 0== num):
        return( sol)
    
    return print_name( num -1, sol + " "+ name, name)

print( print_name( num, sol, name))