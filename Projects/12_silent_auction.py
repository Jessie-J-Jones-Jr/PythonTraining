bidders = {

}

done = False

def run_auction():
    global bidders
    global done
    i = 0
    while not done:
        name = input("What is the bidders name? ").capitalize()
        bid = int(input("What is your bid? $ "))
        bidders[name] = bid
        continue_var = input("Is there another bidder? Yes (Y) or No (N): ").lower().replace("y", "True").replace("n", "No")
        
        if continue_var == "True":
            print("\n"*100)
            print("########################### Next Bidder ###########################")
        else:
            done = True
            print("\n"*100)
            enter = input("Please ENTER to see results...")
            print("\n"*100)
            print("########################### Auction Closed ###########################")
            #print(bidders)
            max_bidder = max(bidders, key=bidders.get)
            max_bid = bidders[max_bidder]
            print(f"{max_bidder} is the highest bidder, with a bid of ${max_bid}!!!!")
            print("\n"*5)
    return bidders

try:
    run_auction()
except ValueError as e:
    print(f"Error: {e}")

