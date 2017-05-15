###################################
#     Computer Project #7
#
#     Facebook Friend Recommendations
#      prompt for file
#      set up matrices
#      error check
#      calculate similarities
#      reccomend a friend
#      ask if user wants to continue
####################################

import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
        aaa_str = sys.stdin.readline()
        aaa_str = aaa_str.rstrip( "\n" )
        print( aaa_str )
    return aaa_str

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
    return file

def read_file(fp):  
    ''' Remember the docstring'''
    # Read n and initialize the network to have n empty lists -- 
    #    one empty list for each member of the network
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])#create empty matrix
    for line in fp:
        line=line.split()
        u=line[0]#fill the matrix with the text file data
        v=line[1]
        network[int(u)].append(int(v))
        network[int(v)].append(int(u))

    return network

def num_in_common_between_lists(list1, list2):
    ''' Calculates the amount of mutual friends'''
    x=0
    for i in list1:
        if i in list2:#count the friends in common
           x+=1
    return x
    
def init_matrix(n):
    '''Create an nxn matrix, initialize with zeros, and return the matrix.'''
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix
    
def calc_similarity_scores(network):  
    '''Creates a similarity matrix of all the similarity scores'''
    similarity_matrix=init_matrix(len(network))
    for i in range(len(network)):
        for j in range(len(network)):#for all friends in matrix calculate 
            #mutual friends
            num_in_common=num_in_common_between_lists(network[i],network[j])
            similarity_matrix[i][j]=int(num_in_common)
            similarity_matrix[j][i]=int(num_in_common)
    return similarity_matrix

def recommend(user_id,network,similarity_matrix):
    '''Recomends the user with most mutual friends'''
    m=0
    mv=0
    user_id=int(user_id)#assign variables
    matrix=similarity_matrix[user_id]
    for i in range(len(network)): #for place values in the length of 
        #the matrices
        if (matrix[i]>mv):
            if i not in network[user_id]:#check to make sure it is the 
                #greatest common friends and not self
                if (i!=user_id):
                    mv=matrix[i]
                    m=i
    return m
    
def main():
    print("Facebook friend recommendation.\n")#lable program
    file=open_file()#open and read the file
    print()
    network=read_file(file)
    similarity_matrix=calc_similarity_scores(network)
    go=True#assign useful variables
    n=len(network)-1
    while go:
        user_id=input('{:s}{:d}{:s}'.format\
                      ("Enter an integer in the range 0 to ",n," : "))
                #prints out range with variable
        try:
            if int(user_id)>=0:#make sure it is positive
                num=recommend(user_id,network,similarity_matrix)
            else:
               print("Error: input must be an int between 0 and",n)
                   #negative error
               continue 
        except:
            print("Error: input must be an int between 0 and",n)
                #out of range or other errors
            continue
        print("The suggested friend for",user_id,"is",num)
        cont=input("\nDo you want to continue (yes/no)? ")
            #to continue or not to continue
        if cont.lower()=="no":
            go=False
            
if __name__ == "__main__":
    main()
#Questions
#Q1: 7
#Q2: 2
#Q3: 1
#Q4: 6
#Q5: 7