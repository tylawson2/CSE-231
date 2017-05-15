
import string

def build_word_set( input_file ):
    
    word_set = set()
    
    for line in input_file:

        # creates a list with each split line
        word_lst = line.strip().split()

        # strips the punctuations from each string in the word list
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        
        for word in word_lst:
            
            if word != "":

                # adding all the words to the word set
                word_set.add( word )
                
    return word_set


def compare_files( file1, file2 ):


    set1=build_word_set(file1)
    set2=build_word_set(file2)
    
    uniq=len(set1|set2)
    print("unique in each: ",uniq)
    both=(len(set1 & set2))
    print("unique in both: ",both)
    
  
######################################################################

f1 = open( "document1.txt" )
f2 = open( "document2.txt" )

compare_files( f1, f2 )

f1.close()
f2.close()

