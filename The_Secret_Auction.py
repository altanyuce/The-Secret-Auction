from art import logo
print(logo)
name_list = []
bid_list = []
any_other_bidders = True
while any_other_bidders == True:
    name = input("What is your name?: ")
    name_list.append(name)
    bid = int(input("What's your bid?: $"))
    bid_list.append(bid)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if other_bidders == "no":
        any_other_bidders = False

bid_list_max = int(max(bid_list))
position = bid_list.index(bid_list_max)

print(f"The winner is {name_list[position]} with a bid of ${bid_list[position]}.")


