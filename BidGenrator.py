bids{}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0;
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished
    name = input("what is your name: ");
    price = int(input("enter your amount: "));
    bids[name]=price
# simran =123
# shri = 547
    should_continue=input("is there any other bidder? type 'yes' or 'no': ")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue=="yes":
        clear()
        find_highest_bidder(bids)
