###################################
#     Computer Project #6
#
#     Password Cracker
#      prompt for type of test
#      get the dictionary if applicable
#      get the zip file
#      run it through the cracker
#      give results to user
####################################

from itertools import product#import modules
import zipfile
import time

def main():
    print("Cracking zip files.")#initial statements
    print("Warning cracking passwords is illegal due to law U.S.C. 1030(6)")
    print("and has a prison term of up to 10 years")
    print()
    a=True#boolean for whole program
    while a:#loops the whole program
        string=input("What type of cracking ('brute force','dictionary','both','q'): ")#prompt user
        if string=="brute force":#brute force testing
           print("\nBrute Force Cracking\n")
           zip_file=open_zip_file()#get zip file
           brute_stuff(zip_file)#send to brute force testing protocol
        if string=="dictionary":#dictionary testing
            print("\nDictionary Cracking\n")
            dict_file=open_dict_file()#get dictionary
            zip_file=open_zip_file()#get zip file
            dict_stuff(zip_file,dict_file)#dictionary protocol
            dict_file.close()#close the dictionary
            zip_file.close()#close the zip file
        if string=="both":#test with both functions
            print("\nBoth Brute Force and Dictionary attack.\n")
            dict_file=open_dict_file()#get dictionary
            zip_file=open_zip_file()#get zip file
            success=dict_stuff(zip_file,dict_file)
                #run the dictionary test protocol
            dict_file.close()#close the dictionary file
            if not success:#if dictionary failed, run brute protocol
                brute_stuff(zip_file)
        if string=="q":#quit if response is "q"
            a=False
        
def brute_stuff(zip_file):
    ''' protocol driver for the brute force attack '''
    start = time.process_time()#start timing
    success=brute_force_attack(zip_file)#run brute force attack
    end = time.process_time()#stop timing
    print('{:<12s}{:<6.4f}'.format("Elapsed time (sec): ",(end-start)))
        #print out elapsed time
    zip_file.close()#close the zip file
    return success#return if the test worked

def dict_stuff(zip_file,dict_file):
    ''' protocol driver for the dictionary attack '''
    start = time.process_time()#start timing
    success=dictionary_attack(zip_file, dict_file)#run actual dict attack
    end = time.process_time()#stop timing
    print('{:<12s}{:<6.4f}'.format("Elapsed time (sec): ",(end-start)))
        #print elapsed time
    return success#send back if it worked
    
def dictionary_attack(zip_file, dict_file):
    ''' attack the password with the dictionary given '''
    for line in dict_file:
        password=line.strip()#strip the passwords from each line
        try: 
            zip_file.extractall(pwd=password.encode())#test password
            result=True#it worked
            break#stop looking
        except:
            result=False#password didnt work
    if result:
        print("Dictionary password is ",password)#if it worked, say password
    else:
        print("No password found.")
    return result#return if it worked or not
 
def open_dict_file():
    '''prompts user for dictionary file name until it works then returns
        pointer'''
    b=True
    while b: 
        s=input("Enter dictionary file name: ")#prompt for file
        try:
            file= open(s,"r")#attempt to open file
            b=False#it worked, stop looking
        except:
            continue
    return file#return pointer

def open_zip_file():
    '''prompts user for zip file name until it works then returns
        pointer'''
    b=True
    while b: 
        s=input("Enter zip file name: ")#prompt for file
        try:
            zip_file = zipfile.ZipFile(s)#attempt to open file
            b=False#it worked stop looking
        except:
            pass
    return zip_file#return pointer

def brute_force_attack(zip_file):
    ''' attack the password with the brute force '''
    result=True
    go=True
    alpha="abcdefghijklmnopqrstuvwxyz"
    while go:     
        for i in range(1,9):#length of 8 characters loop
            if go:
                for items in product(alpha,repeat=i):
                    #use itertools to generate all posibilities
                    password=(''.join(items))#assign password
                    try:
                        zip_file.extractall(pwd=password.encode())
                            #attempt the password
                        go=False#it worked so stop looking
                        result=True
                        break
                    except:
                        result=False
                        go=True
        if go:
            result = False
                #if boolean is still true and you got this far it did not work
        else:
            print("Brute force password is ",password)
                #give password that worked
    return result#return the result if it worked or not

main()

#Questions
#Q1: 7
#Q2: 2
#Q3: 1
#Q4: 6
#Q5: 7