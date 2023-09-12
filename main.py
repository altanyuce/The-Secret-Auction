from ascii import logo 

stop = False
auction = [] # Boş bir liste oluşturuyoruz, bu listede teklifleri saklayacağız.
bid_list = []  # Boş bir liste oluşturuyoruz, bu listede teklif miktarlarını saklayacağız.

print(logo)

while not stop:
    new_auction = {}  # Her bir teklifi bir sözlük olarak saklamak için boş bir sözlük oluşturuyoruz.
    name = input("What is your name? ") # Kullanıcıdan katılımcının adını alıyoruz.
    bid = int(input("What's your bid? $"))  # Kullanıcıdan teklif miktarını alıyoruz.
    answer = input("Anyone else? y/n ") # Başka katılımcı var mı diye soruyoruz.

    new_auction["name"] = name # Oluşturduğumuz sözlüğe katılımcının adını ekliyoruz.
    new_auction["bid"] = bid # Oluşturduğumuz sözlüğe teklif miktarını ekliyoruz.

    auction.append(new_auction) # Katılımcının teklifini açık artırma listesine ekliyoruz.

    bid_list.append(bid) # Teklif miktarını teklif listesine ekliyoruz.
    highest_bid = max(bid_list)  # En yüksek teklif miktarını buluyoruz.
    position = bid_list.index(highest_bid) # En yüksek teklifin hangi konumda olduğunu buluyoruz.
    winner = auction[position]['name'] # Kazananın adını buluyoruz.

    if answer == "n": # Eğer başka katılımcı yoksa döngüyü sonlandırıyoruz.
        stop = True


print(f"The winner is {winner} with a bid of ${highest_bid}")