def real_shuffle():
    global deck
    print(f"==>> deck: {len(deck)}")
 
    
    cut_point = random.randint(22,30)
    items = list(deck.items())
    top_deck = dict(items[:cut_point])
    bottom_deck = dict(items[cut_point:])
    


    while len(in_progress) < 52:
     

        random_number = random.randint(1,4)
   
        

        for i in range(0, random_number):
            is_deck_not_empty = len(top_deck) != 0
            is_not_target_iteration = i != (random_number - 1)
            print(f"Length of top deck {len(top_deck)}")
            print(random_number)

            while is_deck_not_empty and is_not_target_iteration:
                card = random.choice(list(top_deck.keys()))
                in_progress[card] = top_deck.pop(card)
                print("while loop")
                is_deck_not_empty = len(top_deck) != 0
                is_not_target_iteration = i != (random_number - 1)
                i += 1
            i += 1
            

        random_number = random.randint(1,4)
        for i in range(0, random_number):
            is_deck_not_empty = len(bottom_deck) != 0
            is_not_target_iteration = i != (random_number - 1)
            print(f"Length of bottom deck {len(bottom_deck)}")
            print(random_number)
            while is_deck_not_empty and is_not_target_iteration:
                card = random.choice(list(bottom_deck.keys()))
                in_progress[card] = bottom_deck.pop(card)
                print("while loop")
                is_deck_not_empty = len(top_deck) != 0
                is_not_target_iteration = i != (random_number - 1)
                i += 1
            i += 1
            print(f" Deck --{len(in_progress)}")
        print(f"In progress is {len(in_progress)} cards long.")
        print(in_progress)
    
    # deck = in_progress
    # in_progress = {}
    # print(deck)

real_shuffle()