

class Time(object):
    def __init__(self, hour=0, mins=0, secs=0):
        '''creates the three times of the Time clock upon initialization'''
        self.__hour=hour
        self.__mins=mins
        self.__secs=secs
    def __str__(self):
        ''' Return a string (mm/dd/yyyy) to represent a Date. '''
        out_str = "{:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
        return out_str
    def __repr__( self ):
        ''' Return a string as the formal representation a Date. '''
        out_str = "Class Time: {:02d}:{:02d}:{:02d}" \
            .format( self.__hour, self.__mins, self.__secs )
        return out_str
    def from_str(self,str1):
        '''assigns variables from a string'''
        l1=str1.split(':')
        self.__hour=int(l1[0])
        self.__mins=int(l1[1])
        self.__secs=int(l1[2])
        return self