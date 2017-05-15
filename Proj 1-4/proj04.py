###################################
#     Computer Project #4
#
#     Hangman Game
#      prompt for a word
#      test word to make sure it is usable
#      take guesses
#      test guess
#       eventually give results of game
#
####################################


get_word=True #initiallizing several variables and booleans
guess=True
results=""
num_right=0
num_guess=0
dx=0
guess_bin=""
won=False
lost=False
a_guess=True
end=False


print("Hangman: guess letters until you can guess the whole word or phrase.")
print("In this game you get six tries.") #hangman game explainer


while get_word: #while loop for numerical input error check
    word_first=input("\nEnter a word or phrase: ")
    word=word_first.lower()
    if all(x.isalpha() or x.isspace() for x in word):
        print("phrase: ",word_first,) #if no numbers, prints word and breaks
        get_word=False                # while loop
        
    else: #if numbers found, prompts for another input and re-checks it
        print("Error: only letters are allowed as input.")
        
for i in range(len(word)): #constructs a results line for correct guesses
    if(word[i]==" "): 
        results+=" "
    else:
        results+='-'
        
print("current: ",results,) #print statements for guesses and result line
print(num_guess," guesses so far out of 6: ",guess_bin)

while guess: #guessing while loop
    a_guess=True
    char=input("\nGuess a letter or whole word/phrase: ").lower()
        #input line assigned to char var
    if(len(char)==1) and (char.isalpha()):
        dx=0
        for i in range(len(word)): #for loop to find where guess is in phrase
     
            if(char==word[i]):
                results=results[:i]+word_first[i]+results[(i+1):]
                num_right+=1 #slices guess into results line
                dx+=1        # updates several variables
            
        guess_bin+=char
        if(dx==0): #incorrect guess if statement
            print("Letter not in phrase.")
        if(num_right==len(word)): #compares number of correct guesses to len
                                  # (word), if equal, win condition/break while
            guess=False
            won=True
     
    elif all(x.isalpha() or x.isspace() for x in char):#if for full word guess
        if(char==word):
                #if correct, win condition
            won=True
        else:
            print("Wrong guess of whole word or phrase.")
            lost=True #if wrong, loss condition
        end=True    #regardless, update bools to end game
        guess=False
    
    else: #if numbers in guess statementss
        print("Only letters and spaces are allowed as input.")
        a_guess=False
    if a_guess:
        
        num_guess+=1
        if (num_guess==6)and not won:
            guess=False #when out of guesses and no win bools to loss condition
            lost=True
        if lost: #loss printout
            print("You lost.")
        if (guess or won or lost) and not end: #results printout if not booled
           print("current: ",results,)         # to end game
        if won:
            print("You won.") #winner printout
     
            
        
        if not guess and not won: #word reveal printout
           print("The word/phrase was: ",word,)
           
    if not won and not lost: #guess count/guesses print out if not booled
        print(num_guess," guesses so far out of 6: ",guess_bin)
   
#Questions
#Q1: 7
#Q2: 2
#Q3: 1
#Q4: 5
#Q5: 7
       