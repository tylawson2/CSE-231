import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):
        """
        builds matrix from file
        updates self._matrix with new matrix
        """
        n = fp.readline()
        n = int(n)
        floormap = []
        for i in range(n):
            floormap.append(set())
        for line in fp:
            line = line.strip() #line processing
            line = line.split()
            room = int(line[0])
            connection = int(line[1]) #matrix building
            floormap[room-1].add(connection)
            floormap[connection-1].add(room)
        self._matrix = floormap #update self var
        return
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = '{} rooms \nconnections: \n'.format(self.rooms())
        for i in range(len(self._matrix)):
            s += "{}: ".format(i+1) #builds return string with concatenation
            for item in self._matrix[i]:
                s += str(int(item))
                s += " "
            s += "\n"
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return self._matrix[index-1]

    def rooms(self):
        '''Return the number of rooms'''
        return len(self._matrix)
        
def open_file():
   """
   open file function
   includes a bool which bools true if the file exists
   if file not found, prompt for re-input
   returns a file pointer
   """
   filebool = False
   while not filebool:
        try:
            file = input("which file would you like to open? ")
            open(file, "r")
            filebool = True
        except FileNotFoundError:
            print("file does not exist, try again")
            continue
   print("selected file:", file)
   print(" ")
   return open(file, "r")
  
def main():
    file = open_file() #var assignment
    floor = Matrix()
    floor.read_file(file)
    floorlist = []
    for i in range(len(floor._matrix)):
         floorlist.append(i+1)
    end = False #loop bool
    count = 0 #this is the TA count
    while end == False:
        count+=1
        combos = itertools.combinations(floorlist, count)
        for items in combos:
            newmat=set() 
            for y in items:
                newmat |= floor._matrix[y-1]
                newmat.add(y) #adds unions to check for total coverage
            if list(newmat) == (floorlist):
                out = items #if everything ends up equal, solution found
                end = True
                break
    print("{} TA's needed".format(count)) #print statements
    print("Assignments: ", end = "")
    for nums in out:
        print(nums, end = " ")
    print("\n")
    print(floor)
        
main()
