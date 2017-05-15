###################################
#     Computer Project #9
#
#     Co-occurrence checker
#      prompt for file
#      set up Data Dictionary
#      ask for string to check
#      return the co-occurence of the string
#      end upon entry of q
#      
####################################

#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#        aaa_str = sys.stdin.readline()
#        aaa_str = aaa_str.rstrip( "\n" )
#        print( aaa_str )
#    return aaa_str

import string

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

def read_data(fp):
    '''reads file and puts data into dictionary'''
    Data_dict={} 
    lnum=0#instantiate variables
    j=False
    for line in fp:#iterate lines in file
        lnum+=1
        line=line.lower().strip().strip(string.punctuation).split()
            #make lower case and remove punctuation
        for i in line:#iterate words in line
            hi=True
            for j in i:#iterate characters in word
                if j=="'" or j=="-" or j=="." or j==",":
                    #check for punctuation in words
                    x=i.index(j)
                    if x==len(j)+1:#remove extra marks
                        i=i[:x]
                    else:
                        i=i[:x]+i[(x+1):]
                elif not j.isalpha():
                    line.remove(i)   
                    hi=False
            if len(i)<2 and i in line:#check length
                line.remove(i)
                hi=False
            if hi and (i not in Data_dict) and i!="":#add to data dict
                i=str(i)
                a=set()
                a.add(lnum)
                Data_dict[i]=a
                
            elif hi and i!="":#add to data dict
                Data_dict[i].add(lnum)
    return Data_dict

def find_cooccurance(D, input_str):
    '''finds the co-occurences with the string and data dictionary'''
    l1=input_str.split()#makes list from user input
    for i in l1:#iterate user input
        i=i.lower()#set to lower
        for j in i:#iterate each word in response to check for extra symbols
            if j=="'" or j=="-":
                x=i.index(j)
                i=i[:x]+i[(x+1):]                
    lines=set()#create empty set
    first=True
    good=True
    for i in l1:#calculate co occurences
        if first:
            try:
                lines|=D[i]
                first=False
            except:
                lines=None
                good=False
        elif good:
            lines&=D[i]
    try:
        lines=sorted(list(lines))#make sorted list from the set
    except:
        lines=None#return none if necessary
    if input_str=="":
        lines=None
    return lines

def main():
    file=open_file()#get file and open it
    dic=read_data(file)#send it to make data dictionary
    resp=input("Enter space-separated words: ")#ask user for string to check
    resp1=resp.lower()#set to lowercase
    for j in resp1:#iterate to check for extra symbols
        if j=="'" or j=="-":
            x=resp1.index(j)
            resp1=resp1[:x]+resp1[(x+1):]
    while resp1!="q":#check for the quit command
        str2=""
        print('{}{}{}'.format("The co-occurance for ",resp,":"))
        l=find_cooccurance(dic,resp1)#send to find co-occurance
        try:#make it a pretty string response
            for i in l:
                if i!=l[-1]:
                    str2+=str(i)+", "
                else:
                    str2+=str(i)
        except:
            str2=l
        print('{}{}'.format("Lines: ",str2))#output results
        print()
        resp=input("Enter space-separated words: ")#go again
        resp1=resp.lower()
        for j in resp1:
            if j=="'" or j=="-":
                x=resp1.index(j)
                resp1=resp1[:x]+resp1[(x+1):]
    file.close()#close the file pointer
if __name__ == "__main__":#call main
    main()
            
#Questions
#Q1: 6
#Q2: 3
#Q3: 2
#Q4: 6
#Q5: 7  
                    
