import itertools

class Matrix(object):
    '''Add your docstring here.'''
    
    def __init__(self):  # no modification is needed for this method, but you may modify it if you wish to
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):
        n = fp.readline()
        n = int(n)
        floormap = []
        for i in range(n):
            floormap.append(set())
        for line in fp:
            line = line.strip()
            line = line.split()
            room = int(line[0])-1
            connection = int(line[1])-1
            floormap[room].add(connection+1)
            floormap[connection].add(room+1)
        self._matrix = floormap
        return
            
    def __str__(self):
        '''Return the matrix as a string.'''
        s = '{} rooms \nconnections: \n'.format(self.rooms())
        for i in range(len(self._matrix)):
            s += "{}: ".format(i+1)
            for item in self._matrix[i]:
                s += str(int(item)+1)
                s += " "
            s += "\n"
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return self._matrix[index]

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
   
file = open("test1.txt", "r")
floor = Matrix()
floor.read_file(file)

floorlist = []
for i in range(len(floor._matrix)):
    floorlist.append(i+1)
    
    
end = False
count = 1
while end == False:
    combos = itertools.combinations(floorlist, count)
    for items in combos:
        newmat=set()
        for x in items:
            for y in items:
                newmat = newmat | floor._matrix[y-1]
                newmat.add(y)
                
            if len(newmat) == len(floorlist):#should be if newmat is the same as the list of rooms
                print("ayy", items)
                end = True
                break
            
        
    count += 1
    
print("{} TA's needed".format(count))
print("Assignments: ", end = "")
for nums in items:
    print(nums, end = " ")