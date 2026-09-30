def changedue(paid, price):
    return paid-price
price=30
print(f"This Ticket costs Rs.{price}")
print("Accepted Coins: 1, 5, 10, 25")
totalinserted=0
totalcoins=0
while True:
    coins=int(input("Enter a coin (1, 5, 10, 25): "))
    if coins!=1 and coins!=5 and coins!=10 and coins!=25:
        print("Invalid Coin Entered, Try Again...")
        continue
    totalcoins+=1
    totalinserted+=coins
    print("Amount Paid: ", totalinserted)
    print("Coins Inserted: ", totalcoins)
    if totalinserted>=price:
        print("Enough Money inserted!")
        break
if totalinserted>price:
    change=changedue(totalinserted, price)
    print(f"Change due is Rs. {change}")
else:
    pass
print("-------------PURCHASE SUMMARY--------------")
print("PRICE: ", price)
print("AMOUNT PAID: ", totalinserted)
print("COINS INSERTED: ",totalcoins)
print("TOTAL CHANGE: ", change)
print("-------------------------------------------")