
################################################################################
## Demonstration program for class Date
################################################################################

import date
try:
    A = date.Date( 1, "t", 2014 )

    print( A )
    print( A.to_iso() )
    print( A.to_mdy() )
    print( A.is_valid() )
    print()
except:
    print("invalid")

B = date.Date( 12, 31, 2014 )

print( B )
print( B.to_iso() )
print( B.to_mdy() )
print( B.is_valid() )
print()
try:
    C = date.Date()
    C.from_iso( "20 14-0 7-0 4" )
    print( C )
    print( C.to_iso() )
    print( C.to_mdy() )
    print( C.is_valid() )
    print()
except:
    print("invalid")
try:
    D = date.Date()
    
    D.from_mdy( "Mar ch 15, 2015" )
    
    print( D )
    print( D.to_iso() )
    print( D.to_mdy() )
    print( D.is_valid() )
    print()
except:
    print("invalid")
try:
    
    E = date.Date()
    
    print( E )
    print( E.to_iso() )
    print( E.to_mdy() )
    print( E.is_valid() )
    print()
except:
    print("invalid")





