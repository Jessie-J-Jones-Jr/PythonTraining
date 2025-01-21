import random
from deck import deck

my_hand = {}
in_progress = {}
shuffled_deck = {}
shuffled_deck2 ={}

dealer_hand = {}
players_hand = {}
dealer_cards = ()
player_cards = ()
card_count = 2


def shuffle():
    global deck
    global shuffled_deck
    global in_progress

    
    for i in range(52):
        card = random.choice(list(deck.keys()))
        shuffled_deck[card] = deck.pop(card)
        i += 1
    
    deck = shuffled_deck
    shuffled_deck ={}
    
    return deck

#shuffle()
def dealer_shuffle():
    global deck
    global shuffled_deck
    for i in range(130):
        shuffle()
        i += 1

def deal():
    global deck
    global dealer_hand    
    global players_hand

    
    
    card = next(iter(deck))
    players_hand[card] = deck.pop(card)
    
    card = next(iter(deck))
    dealer_hand[card] = deck.pop(card)
    dealer_hand[card]["show"] = "no"

    card = next(iter(deck))
    players_hand[card] = deck.pop(card)
    
    card = next(iter(deck))
    dealer_hand[card] = deck.pop(card)
    
    keys_dealer = list(dealer_hand.keys())
    keys_player = list(players_hand.keys())
    print(f"Dealers Hand {dealer_hand}")
    print(f"Players Hand {players_hand}")

    dealer_cards = dealer_hand[keys_dealer[0]]["face"] + dealer_hand[keys_dealer[0]]["symbol"], dealer_hand[keys_dealer[0]]["value"], dealer_hand[keys_dealer[1]]["face"] + dealer_hand[keys_dealer[1]]["symbol"], dealer_hand[keys_dealer[1]]["value"]
    player_cards =  players_hand[keys_player[0]]["face"] + players_hand[keys_player[0]]["symbol"] , players_hand[keys_player[0]]["value"] , players_hand[keys_player[1]]["face"]+ players_hand[keys_player[1]]["symbol"], players_hand[keys_player[1]]["value"]
    
    print(f"DEALER HAND: ##  and {dealer_cards[2]}. The DEALER has {dealer_cards[3]}PTS")
    print(f"PLAYER HAND: {player_cards[0]}  and {player_cards[2]}. The PLAYER has {player_cards[1] + player_cards[3]}PTS")
    return dealer_hand, players_hand, dealer_cards, player_cards


def hit_stand():
    global deck
    global players_hand
    global card_count
    new_player_cards = []
    hit_or_stand = input("Would you like to HIT (H) or STAND (S)?").lower()
    if hit_or_stand == "s":
        print(players_hand)
        return
    elif hit_or_stand == "h":
        #Picking a the unknown but NEXT key from the Deck dictionary
        card = next(iter(deck))
        #Using that key to put the card from the top of the deck in the players hand
        players_hand[card] = deck.pop(card)
        #Getting all of the unknown key values from the dictionary to iterate through
        keys_player = list(players_hand.keys())

        #Debug Prints
        #print(players_hand)
        #print(keys_player)
        #iterating through to create a new player card list (previous used a tuple by accident need to homogenize it)
        
        for i in range(card_count+1):
            
            new_player_cards += [players_hand[keys_player[i]]["face"] + players_hand[keys_player[i]]["symbol"]]
            new_player_cards += [players_hand[keys_player[i]]["value"]]
        card_print ="PLAYER HAND: " 
        card_print2 = "==> SCORE: "
        card_print3 = 0  
        for i in range((card_count+1)*2):
            if i % 2 == 0: 
                card_print +=  new_player_cards[i] + " "
            else:
                card_print3 +=  new_player_cards[i]
    #Wanted to create a recursion but I think it best to do that in a formal try except block        
    else:
        print("You must type H or S ...")
        hit_or_stand()
    #can't access this might have to make the above a list would be easier append that way
    print(f"DEALER HAND: ##  and {dealer_cards[2]}. The DEALER has {dealer_cards[3]}PTS")
    
    print("PLAYER HAND :"+ card_print,card_print2,card_print3)

try:
    dealer_shuffle()
    print(shuffled_deck)
    input("To Deal Hand press ENTER ... ")
    print(deck)
    deal()
    hit_stand()
except ValueError as e:
    print(f"Error: {e}")
