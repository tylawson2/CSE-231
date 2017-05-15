import clock


A = clock.Time( 1, 3, 2 )

print( A )
print( A.__str__() )
print( A.__repr__() )
A.from_str("04:34:22")
print(A.__str__())