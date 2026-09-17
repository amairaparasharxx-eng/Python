def changedue(paid, price):
    return paid-price
snackprice=25
print("---------SNACK VENDING MACHINE------------")
print(f"This Snack costs Rs.{snackprice}")
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
    if totalinserted>=snackprice:
        print("Enough Money inserted!")
        break
print("Dispensing Snack...")
if totalinserted>snackprice:
    change=changedue(totalinserted, snackprice)
    print(f"Change due is Rs. {change}")
else:
    pass
print("-------------PURCHASE SUMMARY--------------")
print("SNACK PRICE: ", snackprice)
print("AMOUNT PAID: ", totalinserted)
print("COINS INSERTED: ",totalcoins)
print("TOTAL CHANGE: ", change)
print("-------------------------------------------")