import Blind_Auction_art

print(Blind_Auction_art.logo)

auction_info = {}

should_continue = True

while should_continue: 
    name = input("What is your name? ")

    while True: 
        try: 
            bid = int(input("What is your bid? $"))
            break
        except ValueError:
                print("Invalid input. Please enter a number (digits only).")

    auction_info[name] = bid
    
    while True: 
        restart = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
        if restart in ["yes","no"]:
            break 
        else: 
            print("Invalid input. Please type 'yes' or 'no'.")

    if restart == "no":
        should_continue = False 
    else:
        print("\n" * 20)

highest_bid = 0
winner = ""
for bidder in auction_info:
    bid_amount = auction_info[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}")





#       This code can be modified with these two tasks to make it better:
#       1- what if there is a tie? 
#       2- what if there is two or more names that are the same?  