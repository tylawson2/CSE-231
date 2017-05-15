
##
## Demonstrate some of the operations of the Pet classes
##

import pets

def main():
    
    try:

        # Hamster
        A = pets.Pet( "Hamster" )
        print( A )       
        
        # Dog named Fido who chases Cats
        B = pets.Dog( "Fido" )
        print( B )

        # Cat named Fluffy who hates everything
        C = pets.Cat( "Fluffy", "everything" )
        print( C )
        
        E = pets.Dog("", "cars")
        print(E)

        F = pets.Cat("Tom", "mice")
        print(F)
        
        D = pets.Pet("Susan", "Alligator")
        print(D)

        
    except pets.PetError:
        
        print( "Got a pet error." )

main()

