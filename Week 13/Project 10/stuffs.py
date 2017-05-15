'''
CSE 231 Project 10
Algorithm:
    Setup and display game
    Display commands menu
    Request command
    Check validity of move
    Execute move
    Display result
    Rerequest command
'''

import cards #This is necessary for the project


BANNER = """
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
   
     
def valid_fnd_move(src_card, dest_card):
    """
    Take the source and destination cards, determine if proposed move is valid
    """
    #if no card in fnd and src_card is an ace, its a valid move
    if dest_card == None and src_card.rank() == 1:
        return #if src_card not an ace, move is invalid
    elif dest_card == None and src_card.rank() != 1:
        raise RuntimeError("Only an ace can be put into an empty foundation.")
    #if same suit and dest card 1 less than src card, move is valid
    if dest_card.suit() == src_card.suit() and \
    src_card.rank()-dest_card.rank() == 1:
        return #if not same suit, invalid
    elif dest_card.suit() != src_card.suit() and \
    src_card.rank()-dest_card.rank() == 1:
        raise RuntimeError("These suits do not match.")
    #if dest card not 1 less than src card, invalid
    elif dest_card.suit() == src_card.suit() and \
    src_card.rank()-dest_card.rank() != 1:
        raise RuntimeError("The difference between these cards is not 1.")
    #if both above things are wrong, invalid
    elif dest_card.suit() != src_card.suit() and \
    src_card.rank()-dest_card.rank() != 1:
        raise RuntimeError("Nothing remotely correct about this.")
  
      
def valid_tab_move(src_card, dest_card):
    """
    Take the source and destination cards, determine if proposed move is valid
    """    
    if dest_card == None: #if tab is empty, valid
        return #if same suit and src card 1 less than dest card, valid
    if dest_card.suit() == src_card.suit() and \
    src_card.rank() + 1 == dest_card.rank():
        return #if dif suit, invalid
    elif dest_card.suit() != src_card.suit() and \
    src_card.rank() + 1 == dest_card.rank():
        raise RuntimeError("These suits do not match.")
        #if src card not 1 less than dest card, invalid
    elif dest_card.suit() == src_card.suit() and \
    src_card.rank() + 1 != dest_card.rank():
        raise RuntimeError("The difference between these cards is not 1.")
        #if everything wrong, invalid
    elif dest_card.suit() != src_card.suit() and \
    src_card.rank() + 1 != dest_card.rank():
        raise RuntimeError("Nothing remotely correct about this attempt.")
    
def tableau_to_cell(tab, cell):
    """
    Take tableau and cell, move last card of tableau to proposed cell if valid
    """  
    if tab == []: #if no card in selected tab raise error 
        raise RuntimeError("You can't move something from an empty tableau.")
    if cell == []: #if cell empty then move card from tab to cell
        card = tab.pop()
        cell.append(card)
    elif cell != []: #if cell occupide then raise error
        raise RuntimeError("The destination cell is occupied.")
            
            
def tableau_to_foundation(tab, fnd):
    """
    Take tableau and foundation, move last card of tableau to proposed 
    foundation if valid
    """    
    if tab == []:#if no card in selected tab raise error 
        raise RuntimeError("You can't move something from an empty tableau.")
    src_card = tab[-1]
    if fnd == []: #if fnd empty
        dest_card = None
    else: #if card in fnd already
        dest_card = fnd[-1]
    valid_fnd_move(src_card,dest_card)
    card = tab.pop() #move card from tab to fnd
    fnd.append(card)
            
            
def tableau_to_tableau(tab1, tab2):
    """
    Take source tableau and destination tableau, move last card of source 
    tableau to proposed destination tableau if valid
    """    
    if tab1 == []:#if no card in selected tab raise error 
        raise RuntimeError("You can't move something from an empty tableau.")
    src_card = tab1[-1] #src card = last card in tab
    if tab2 == []: #if dest tab empty
        dest_card = None
    else: #else dest card = last card in list
        dest_card = tab2[-1]
    valid_tab_move(src_card,dest_card)
    card = tab1.pop() #move card
    tab2.append(card)


def cell_to_foundation(cell, fnd):
    """
    Take cell and foundation, move card from cell to proposed foundation
    if valid
    """    
    if cell == []:#if no card in selected cell raise error 
        raise RuntimeError("You can't move something from an empty cell.")
    src_card = cell[0] #src card = only card in cell
    if fnd == []: #if fnd empty 
        dest_card = None
    else: #else dest card = last card in fnd list
        dest_card = fnd[-1]
    valid_fnd_move(src_card, dest_card)
    card = cell.pop() #move card
    fnd.append(card)


def cell_to_tableau(cell, tab):
    """
    Take cell and tableau, move card from cell to proposed tableau
    if valid
    """    
    if cell == []:#if no card in selected cell raise error 
        raise RuntimeError("You can't move something from an empty cell.")
    src_card = cell[0]#src card = only card in cell
    if tab == []:#if fnd empty 
        dest_card = None
    else:#else dest card = last card in fnd list
        dest_card = tab[-1]
    valid_tab_move(src_card, dest_card)
    card = cell.pop()#move card
    tab.append(card)
              
              
def is_winner(foundations):
    """
    Take the foundation list, determine if player has won game
    """    
    done = False 
    number_complete = 0
    for i in foundations: #iterate through foundations and check length
        if len(i) == 13 and i[-1].rank() == 13: #if len = 13 and king on top
            number_complete += 1 #then fnd is complete
    if number_complete == 4: #if all fnds complete done = True
        done = True
    if done: #if done true then player has won!
        print(BANNER)
    
    return done


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
    stock = cards.Deck()
    #The game piles are here, you must use these.
    cells = [[], [], [], []]                    #list of 4 lists
    foundations = [[], [], [], []]              #list of 4 lists
    tableaus = [[], [], [], [], [], [], [], []] #list of 8 lists
    
    """ YOUR SETUP CODE GOES HERE """
    stock.shuffle()
    for i in range(7):
        for column in tableaus:
            x = stock.deal()
            column.append(x)
    for tab in tableaus:
        if tab[-1] == None:
            tab.pop()
        
    
    return cells, foundations, tableaus


def display_game(cells, foundations, tableaus):
    """
    Add your function header here.
    """
    #Labels for cells and foundations
    print("    =======Cells========  ====Foundations=====")
    print("     --1----2----3----4--  --1----2----3----4--")
    print("    ", end="")
    
    L_cell = [] #empty list to store items to be displayed
    for i in cells:
        if i == []: #if nothing in cell display [ ]
            L_cell.append('[ ]')
        else: #else append item from cell list to display list
            L_cell.append(i[0])
    L_fnd = []#empty list to store items to be displayed
    for i in foundations:
        if i == []:#if nothing in fnd display [ ]
            L_fnd.append('[ ]')
        else:#else append last item from fnd list to display list
            L_fnd.append(i[-1])
            #print formatting
    print("{:>5s}{:>5s}{:>5s}{:>5s}    {}{:>5s}{:>5s}{:>5s}".format( \
          str(L_cell[0]),str(L_cell[1]), \
          str(L_cell[2]),str(L_cell[3]),str(L_fnd[0]), \
            str(L_fnd[1]),str(L_fnd[2]), \
            str(L_fnd[3])))

    print()
    #Labels for tableaus
    print("    =================Tableaus=================")
    print("    ---1----2----3----4----5----6----7----8---")
    #max_length finds max number of rows needed for tab display
    max_length = max([len(x) for x in tableaus])
    for i in range(max_length):
        L = []#empty list to store items to be displayed
        for tab in tableaus:
            if len(tab) > i:#check if tab has item for this column
                L.append(tab[i])#if so append
            else:#else append empty string
                L.append('')    
        #print formatting
        print("{:>9s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}{:>5s}".format( \
        str(L[0]),str(L[1]),str(L[2]),str(L[3]),str(L[4]),str(L[5]), \
        str(L[6]),str(L[7])))
    
        
    
#HERE IS THE MAIN BODY OF OUR CODE
print(RULES)
cells, fnds, tabs = setup_game()
display_game(cells, fnds, tabs)
print(MENU)
command = input("prompt :> ").strip().lower() #request command
while command != 'q':
    command_list = list(command)
    command = ''
    for i in command_list: #creates string of command input
        if i != ' ':
            command += i
    try:
        if len(command) != 4: #check for invalid input
            raise RuntimeError("Command must be as specified in menu.")
        if command == 'h': #based on input, call related function(s)
            print(MENU)
        if command == 'r':
            print(RULES)
            print(MENU)
            cells, fnds, tabs = setup_game()
        if command[:2] == 'tc':
            tableau_to_cell(tabs[int(command[2])-1], cells[int(command[3])-1])
        if command[:2] == 'tf':
            tableau_to_foundation(tabs[int(command[2])-1], \
                                       fnds[int(command[3])-1])
        if command[:2] == 'tt':
            tableau_to_tableau(tabs[int(command[2])-1], \
                                    tabs[int(command[3])-1])
        if command[:2] == 'cf':
            cell_to_foundation(cells[int(command[2])-1], \
                                     fnds[int(command[3])-1])
        if command[:2] == 'ct':
            cell_to_tableau(cells[int(command[2])-1], tabs[int(command[3])-1])
        
    #Any RuntimeError you raise lands here
    except RuntimeError as error_message:
        print("{:s}\nTry again.".format(str(error_message)))
    except IndexError:
        print('Invalid index in command.')
        print('Try again.')
    
    done = is_winner(fnds) #winner?
    if done:#yes? then display final result and end game.
        display_game(cells, fnds, tabs) 
        command = 'q'
    else:
        display_game(cells, fnds, tabs)                
        command = input("prompt :> ").strip().lower()


