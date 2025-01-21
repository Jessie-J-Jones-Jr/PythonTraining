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

dealer_shuffle()
print(shuffled_deck)

input("To Deal Hand press ENTER ... ")

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
    
    print(f"DEALER HAND: ## and {dealer_cards[2]}. The DEALER has {dealer_cards[3]}PTS")
    print(f"PLAYER HAND: {player_cards[0]} and {player_cards[2]}.  The PLAYER has {player_cards[1] + player_cards[3]}PTS")
    return dealer_hand, players_hand
print(deck)
deal()

def hit_stand():
    global dealer_hand
    global players_hand
    hit_or_stand = input("Would you like to HIT or STAND?")