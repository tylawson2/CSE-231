
##
## Class PetError -- complete
##

class PetError( ValueError ):
    
    pass

##
## Class Pet -- not complete
##

class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        
        lis = ["dog", "cat", "horse", "gerbil", "hamster", "ferret"]
        if species.lower() in lis:
            
            self.__species_str = species.title()
            self.__name_str = name.title()
            
        else:
            
            raise PetError()
            
    def __str__( self ):
        
        if self.__name_str:
            result_str = "species of {:s}, named {:s}".format(self.__species_str, self.__name_str)
        else:
            result_str = "species of {:s}, unnamed".format(self.__species_str)
        return result_str

##
## Class Dog -- not complete
##

class Dog( Pet ):

    def __init__(self, name = '', chases = "Cats"):
        self.chases = chases
        super().__init__("dog", name)
    
    def __str__(self):
        
        return_str = "{:s}, chases {:s}".format(super().__str__(), self.chases)
        return return_str
            
##
## Class Cat -- not complete
##

class Cat( Pet ):
    
    def __init__(self, name = '', hates = "Dogs"):
        
        self.hates = hates
        super().__init__("cat", name)
    
    def __str__(self):
        
        return_str = "{:s}, hates {:s}".format(super().__str__(), self.hates)
        return return_str
