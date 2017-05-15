
import cards

def mod_rank(card):
    return (14 if card.rank() == 1 else card.rank())

def compare (card1, card2):
    one = mod_rank(card1)
    two = mod_rank(card2)
    if one == two:
        winner = 0
    elif one > two:
        winner = 1
    else:
        winner = 2
    return winner
        
def battle(hand1, hand2):
    card1 = hand1.pop(0)
    card2 = hand2.pop(0)
    print("player 1 played", card1)
    print("player 2 played", card2)
    if compare(card1, card2) == 0:
        hand1.append(card1)
        hand2.append(card2)
    elif compare(card1, card2) == 1:
        hand1.append(card1)
        hand1.append(card2)
    else:
        hand2.append(card1)
        hand2.append(card2)
    print("player 1's hand: ", hand1)
    print("player 2's hand: ", hand2)
    return hand1, hand2
    
def winner (hand1, hand2):
    one = len(hand1)
    two = len(hand2)
    if one == two:
        winner = 0
    elif one > two:
        winner = 1
    else:
        winner = 2
    return winner
        
# Create the deck of cards

the_deck = cards.Deck()
the_deck.shuffle()

player1_list=[]
player2_list=[]
for i in range( 5 ):
    player1_list.append( the_deck.deal() )
    player2_list.append( the_deck.deal() )
    
while len(player1_list) and len(player2_list):
    players = battle(player1_list, player2_list)
    player1_list = players[0]
    player2_list = players[1]
    if not player1_list or not player2_list:
        break
    cont = input()
    if cont:
        break

print("player", winner(player1_list, player2_list), "wins!")