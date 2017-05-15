###################################
#     Computer Project #5
#
#     Ceaser Cipher
#      prompt for cipherText
#      get most common character and its shift
#      shift characters
#      print output in upper case
#      prompt user if its readable english
#       if yes: end program
#       else: run again
#
####################################
'''
import sys
def input( prompt=None ):
    if prompt != None:
        print( prompt, end="" )
    aaa_str = sys.stdin.readline()
    aaa_str = aaa_str.rstrip( "\n" )
    print( aaa_str )
    return aaa_str
'''


def get_char(ch,shift):
    '''gets the character based off of the shift'''
    ch=chr(ord(ch)+int(shift))#shifts character with ascii code
    if 65<=ord(ch)<=90 or 97<=ord(ch)<=122:#test if in alphabet
        pass
    else:    
        ch=chr(ord(ch)+26)#put it back in alphabet
    return ch#return shifted character

def get_shift(str,ignore):
    ''' gets the shift to the new characters'''
    first=True#boolean for first time in for loop
    mc=''#most common character variable
    for i in str:#find most common character
        if first:
            mc=i
            first=False
        if str.count(i)>= str.count(mc) and i.isalpha() and i not in ignore:
            mc=i
    shift=ord("e")-ord(mc)
    return mc,shift# return both most common character and the shift key
    

    
    
def output_plaintext(s,shift):
    '''Outputs the shifted plain text'''
    out_text=""#instantiate string
    for i in s:#write out new text
        if i.isalpha():
            out_text+=get_char(i, shift)
        else:
            out_text+=i
 
    return out_text
        
        
def main():
    go=True   ##instantiate variables
    bad_letter=""
    mc=""
    tup=(0,"")
    print("Cracking a Caesar cypher.\n\n")
    while go:
        da_string = input("Input cipherText: ")#prompt for text
        tup=get_shift(da_string,bad_letter)
            #get the shift key and most common character
        mc=tup[0]# assign variables from tuple
        shift=tup[1]
        print()
        print(output_plaintext(da_string,shift).upper())#print out result
        testing=True
        while testing:#see if it is readable
            test=input("Is the plaintext readable as English? (yes/no): ")
            if test=="no":#if no, run try again
                bad_letter+=mc
                tup=get_shift(da_string,bad_letter)#get new shift
                shift=tup[1]
                mc=tup[0]
                print(output_plaintext(da_string,shift).upper())#new text
            elif test=="yes":#end when correct
              
                go=False
                testing=False
            else:
                print("\nThat was not a valid response, try again.\n")
                testing=True
   
 
if __name__ == "__main__": 
    main()
