###################################
#     Computer Project #11
#
#     TA Room assign
#      prompt for file
#      set up matrix and string
#      calculate how many TAs needed and their room assignments
#        with greedy algorithm
#      return results
#
####################################

import itertools

class Matrix(object):
    '''This is the adjacency Matrix'''
    
    def __init__(self): 
        '''Create and initialize your class attributes.'''
        self._matrix = []
        self._rooms = 0
        
    def read_file(self,fp):  #fp is a file pointer
        '''Build an adjacency matrix that you read from a file fp.'''
        self._rooms=int(fp.readline().strip())#assign amount of rooms
        for i in range(self._rooms):#set up list of empty sets
            self._matrix.append(set())
        for line in fp:#add values from the txt file
            line=line.strip().split()
            for i in line:
                n=int(i)
                self._matrix[n-1].add(int(line[line.index(i)-1]))
        fp.close()#close txt file
               
    def __str__(self):
        '''Return the matrix as a string.'''
        s = 'Adjacency Matrix\n'
        x=1
        for i in self._matrix:
            l=sorted(i)
            s+='{}{}'.format(x,": ")#room number 
            for y in l:
                s+='{}{}'.format(y," ")#each floor adjacent
            s+="\n"
            x+=1
        return s  #__str__ always returns a string

    def __repr__(self):  # no modification need of this method
        '''Call __str__() to return a string for displaying in the shell'''
        return self.__str__()  
        
    def adjacent(self,index):
        '''Return the set of connecting rooms to room specified by index'''
        return self._matrix[int(index)-1]

    def rooms(self):
        '''Return the number of rooms'''
        return len(self._matrix)
                
def open_file():
    '''prompt user and open a file'''
    go=True
    while go:
        file=input("Enter a filename: ")#ask for file
        try:
            file=open(file,"r")#try to open it
            go=False
        except:
            print("Error in filename.")#account for errors
            go=True
    print()
    return file

def main():
    m=Matrix()#set up adjacency matrix
    fp=open_file()#open test file
    m.read_file(fp)#set up the matrix
    done=False#useful variables
    cov=set()
    numT=0
    while not done:#keep going until number of TAs is found
        numT+=1#add 1 each time through
        rooms=list(range(1,len(m._matrix)+1))#list of rooms
        pos=itertools.combinations(rooms,numT)#get room possibilities
        for i in pos:#for all possibilities
            for x in i:#for all room assignments in each possibility
                cov|=m._matrix[x-1]#union of the adjacent rooms
                cov.add(x)#add room assignment too covered set
            if sorted(cov)==rooms:#check if all rooms covered
                done=True
                loc=i#take rooms assigned when it works
                break  
            else:
                cov=set()#make covered a blank set again for next time through
    loc=sorted(loc)#make sorted list of the room assignments
    for i in loc:
        loc[loc.index(i)]=str(i)
    s=", ".join(loc)
    print("TAs needed: ",numT)#print out results
    print("TAs assigned to rooms: ",s)
    print()    
    print(m)#print adjacency matrix

if __name__ == "__main__":
    main()