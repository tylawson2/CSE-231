
import string
from operator import itemgetter


def add_word( word_map, word ):
    '''adds words to a word map'''
    #if the word being tested is not in the document instantiate it
    if word not in word_map and (word != " ") :
        word_map[ word ] = 0

    # add value to the spot
    word_map[ word ] += 1


def build_map( in_file, word_map ):
    '''building the word map'''
    for line in in_file:

        # make a list from each line in document
        word_list = line.split()

        for word in word_list:

            # for every word in the line, strip it and add it 
            word = word.strip().strip(string.punctuation).lower()
            if not word=="":
                add_word( word_map, word )
        

def display_map( word_map ):
    '''sets up and prints the word map'''
    word_list = list()

    # adding words with their count
    for word, count in word_map.items():
        word_list.append( (word, count) )

    # sorts the list 
    word_list=sorted(word_list)
    
    freq_list = sorted( word_list, key=itemgetter(1) )

    print( "\n{:15s}{:5s}".format( "Word", "Count" ) )
    print( "-"*20 )
    for item in freq_list:
        print( "{:15s}{:>5d}".format( item[0], item[1] ) )


def open_file():
    '''opens the file it is told to'''
    str1= input("Input a file: ")
    try:
        in_file = open( str1, "r" )
        
    except IOError:
        print( "\n*** unable to open file ***\n" )
        in_file = None

    return in_file


word_map = dict()
in_file = open_file()

if in_file != None:

    build_map( in_file, word_map )
    display_map( word_map )
    in_file.close()

