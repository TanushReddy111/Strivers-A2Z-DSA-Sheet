string = str( input( "Enter a String:- "))

def solve( string):
    if string == string[:: -1]:
        return True
    else:
        return False
    

print( solve( string))
