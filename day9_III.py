print(" Welcome to the secret auction program")
bids = {}
bidding_finished = False

while not bidding_finished :
    name = input("Enter your name : ")
    bid = int(input("Enter your bid : "))
    bids[name] = bid
    should_continue = input("Are there any other bidders ? Type 'yes' or 'no' : ".lower())
    if should_continue == "no": 
        bidding_finished = True
        highest_bid = 0
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print (f"The winner is {winner} with a bid of {highest_bid}")

    else :
        print("\n" * 50)