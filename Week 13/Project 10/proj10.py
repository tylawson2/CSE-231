###################################
#     Computer Project #10
#
#     Baker's Game
#      setup game
#      ask for moves
#      error check
#      show game board after each move
#      end if won or "q" is hit
####################################

import cards1 #import card class

WIN = """
    __        _____ _   _ _   _ _____ ____  _ _ _ 
    \ \      / /_ _| \ | | \ | | ____|  _ \| | | |
     \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |
      \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|
       \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)

"""

RULES = """
     ____        _             _        ____
    | __ )  __ _| | _____ _ __( )___   / ___| __ _ _ __ ___   ___
    |  _ \ / _` | |/ / _ \ '__|// __| | |  _ / _` | '_ ` _ \ / _ \\
    | |_) | (_| |   <  __/ |    \__ \ | |_| | (_| | | | | | |  __/
    |____/ \__,_|_|\_\___|_|    |___/  \____|\__,_|_| |_| |_|\___|

    Cells:       Cells are numbered 1 through 4. They can hold a
                 single card each.

    Foundations: Foundations are numbered 1 through 4. They are
                 built up by rank from Ace to King for each suit.
                 All cards must be in the foundations to win.

    Tableaus:    Tableaus are numbered 1 through 8. They are dealt
                 to at the start of the game from left to right
                 until all cards are dealt. Cards can be moved one
                 at a time from tableaus to cells, foundations, or
                 other tableaus. Tableaus are built down by rank
                 and cards must be of the same suit.

"""

MENU = """

    Game commands:
    
    TC x y    Move card from tableau x to cell y
    TF x y    Move card from tableau x to foundation y
    TT x y    Move card from tableau x to tableau y
    CF x y    Move card from cell x to foundation y
    CT x y    Move card from cell x to tableau y
    R         Restart the game with a re-shuffle
    H         Display this menu of commands
    Q         Quit the game
    
"""
   
  #^Some Variables up there
   
def valid_fnd_move(src_card, dest_card):
    """check validity of move to foundation"""
    if dest_card==None and src_card.rank()==1:#check if movie ace to empty fnd
        return
    elif dest_card==None:#if its empty but not using an ace
        raise RuntimeError("You must start the foundation with an ace.")
    if (src_card.suit()==dest_card.suit() and src_card.rank()==\
    dest_card.rank()+1):#valid build onto a function
        return
    elif src_card.suit()==dest_card.suit():#error check order and others
        raise RuntimeError("The cards are not in the correct order!")
    else:
        raise RuntimeError("Those cards do not work!")
    
def valid_tab_move(src_card, dest_card):
    """Checks validity of tableau move"""  
    if dest_card==None:#check if moving to empty tableau
        return
    if (src_card.suit()==dest_card.suit() and \
        src_card.rank()==dest_card.rank()-1):#check if valid tab move
        return
    elif src_card.suit()==dest_card.suit():#error check value error or other
        raise RuntimeError("The cards are not in the correct order!")
    else:
        raise RuntimeError("Those cards do not work!")    
    
def tableau_to_cell(tab, cell):
    """moves card from tab to cell"""    
    if cell==[]:#if the cell is available, add to it
        cell.append(tab.pop())
    else:#account for full cell
        raise RuntimeError("That cell is full!")        
            
def tableau_to_foundation(tab, fnd):
    """moves card from tab to foundation"""
    if tab==[]:#can't move anything from an empty tab
        raise RuntimeError("That tableau is empty!")
    if fnd==[]:#account for  empty foundation
        card2=None
    else:#otherwise set the top card to the card in use
        card2=fnd[-1]
    card1=tab[-1]
    valid_fnd_move(card1, card2)#check valid move
    card1=tab.pop()#remove from tab
    fnd.append(card1)    #add to  foundation  
            
def tableau_to_tableau(tab1, tab2):
     """moves card from tab to another tab"""
     if tab1==[]:#cant move anything that isnt there
        raise RuntimeError("That tableau is empty!")
     if tab2==[]:#assign none to an empty tab card 
        card2=None
     else:#otherwise assign the value of card in use
        card2=tab2[-1]
     valid_tab_move(tab1[-1], card2)#check validity
     card1=tab1.pop()#remove the card being moved
     tab2.append(card1)#assign it to new spot

def cell_to_foundation(cell, fnd):
    """moves card from cell to foundation"""
    if cell==[]:#checks if anything in the celll
        raise RuntimeError("That cell is empty!")
    if fnd==[]:#placehold for empty foundation
        card2=None
    else:#top card of filled foundation
        card2=fnd[-1]
    card1=cell[-1]#get card from cell
    valid_fnd_move(card1, card2)#check if valid
    card1=cell.pop()#move the card
    fnd.append(card1)

def cell_to_tableau(cell, tab):
    """moves card from cell to a tab"""
    if cell==[]:#check is the cell is empty
        raise RuntimeError("That cell is empty!")
    if tab==[]:#placeholder for empty tab
        card2=None
    else:#card in use assigned
        card2=tab[-1]
    valid_tab_move(cell[-1], card2)#validity check
    card1=cell.pop()#move the card
    tab.append(card1)              
              
def is_winner(foundations):
    """Determines if the user has won or not"""
    win=False    
    for i in foundations:#check all foundations
        if i==[]:#if a foundation is empty, you aint won yet
            return False
            break
        elif i[-1].rank()==13:#possible win if top card king
            win=True
        else:#if top card isnt a king you aint won yet
            return False
            break
    return win

def setup_game():
    """
    The game setup function. It has 4 cells, 4 foundations, and 8 tableaus. All
    of these are currently empty. This function populates the tableaus from a
    standard card deck. 
    Tableaus: All cards are dealt out from left to right (meaning from tableau
    1 to 8). Thus we will end up with 7 cards in tableaus 1 through 4, and 6
    cards in tableaus 5 through 8 (52/8 = 6 with remainder 4).
    This function will return a tuple: (cells, foundations, tableaus)
    """
    #You must use this deck for the entire game.
    #We are using our cards.py file, so use the Deck class from it.
    stock = cards1.Deck()#set up deck
    stock.shuffle()#shuffle deck   
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []]#list of 8 lists
    x=0
    while not stock.is_empty():
        tableaus[x].append(stock.deal())#put deck into tableaus list of lists
        x+=1
        if x==8:
            x=0
    return cells, foundations, tableaus

def display_game(cells, foundations, tableaus):
    """displays the game board in the console"""
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")
    pcells=[]
    for i in cells:#print out current cells
        try:
            pcells.append("[ "+str(i[-1])+"]")
        except:
            pcells.append("[   ]")
    for i in foundations:#print out current foundations
        try:
            pcells.append("[ "+str(i[-1])+"]")
        except:
            pcells.append("[   ]")
    print('{:>6s}{:3s}{:3s}{:3s}{:>7s}{:3s}{:3s}{:3s}'\
          .format(*(x for x in pcells)))
    # to print a card using formatting, convert it to string:
    # print("{}".format(str(card)))
    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    max=0
    for i in tableaus:#find longest tab
        if len(i)>max:
            max=len(i)
    for y in range(max):#print out the game board
        print("       ",end="")
        l1=[]
        for x in tableaus:
            if len(x)>y:
                l1.append(str(x[y]))
            else:
                l1.append('')
        print('{:5}{:5}{:5}{:5}{:5}{:5}{:5}{:5}'.format(*(i for i in l1),end=""))
        
def commander(com, tableaus, fnds, cells):
    '''additional function to control the commands'''
    go=True#boolean for if it is a control
    if com[0].lower()=="tt":#tab to tab command
        tableau_to_tableau(tableaus[int(com[1])-1], tableaus[int(com[2])-1])  
        go=False
    if com[0].lower()=="tf":#tab to fnd command
        tableau_to_foundation(tableaus[int(com[1])-1], fnds[int(com[2])-1])
        go=False
    if com[0].lower()=="tc":#tab to cell command
        tableau_to_cell(tableaus[int(com[1])-1], cells[int(com[2])-1])
        go=False
    if com[0].lower()=="cf":#cell to fnd
        cell_to_foundation(cells[int(com[1])-1], fnds[int(com[2])-1])
        go=False
    if com[0].lower()=="ct":#cell to tab
        cell_to_tableau(cells[int(com[1])-1], tableaus[int(com[2])-1])
        go=False
    if com[0].lower()=="h":#h for print menu
        print(MENU)
        go=False
    if com[0].lower()=="q":#quit game
        go=False
    if go:#raise error for invalid command
        raise RuntimeError("You're input was invalid")
    
def main():
    print(RULES)
    hi=True
    cells, fnds, tabs = setup_game()#assign variables from the game setup
    display_game(cells, fnds, tabs)#show the game board
    print(MENU)
    com = input("prompt :> ").strip().lower().split()#command input to list
    print()
    while com[0].lower() != "q":#while command not quit
        hi=True
        try:#try in case of error raised
            if com[0].lower()=="r":#reset game
                print(RULES)
                cells, fnds, tabs = setup_game()
                display_game(cells, fnds, tabs)
                print(MENU)
                com = input("prompt :> ").strip().lower().split()
                hi=False
            else:    #run through the command function that was made
                commander(com, tabs, fnds, cells)
        except RuntimeError as error_message:#except clause to catch errors 
            print("{:s}\nTry again.".format(str(error_message)))
        if is_winner(fnds):#check win status
            print(WIN)
            break
        elif hi:#if you didnt reset it, go for next turn
            if com[0].lower()!="h":
                display_game(cells, fnds, tabs)                
            com = input("prompt :> ").strip().lower().split()
            print()

if __name__ == "__main__":#call main
    main()
