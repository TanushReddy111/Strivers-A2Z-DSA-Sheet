string = str( input( "Enter a string:- "))
end = len(string)
first = 0
def solve( string, end, first):

    if ( first > end):
        return True
    
    if string[first] == string [end]:
        return solve( string, end -1, first +1)
    return False

print( solve( string, end -1, first))