def greeting():
    print("Hello! Welcome to the lemonade stand")
    print("Fresh Lemonade just for You!!")
greeting()
cupprice=float(input("Enter Price of 1 Cup: "))
cupssold=int(input("Enter Total Number of Cups sold: "))
def cal_total(price, cup):
    total=price*cup
    return total
totalcost=cal_total(cupprice, cupssold)
print("Total: ", totalcost)
paid=float(input("Enter Amount Paid: "))
def cal_change(paid1, total1):
    change=total1-paid1
    return change
due=cal_change(paid, totalcost)
print("Change: ", due)
print("-----------RECIEPT-------------")
print(f"Cup Price: {cupprice}")
print(f"Cups Sold: {cupssold}")
print(f"Total Cost: {totalcost}")
print(f"Amount Paid: {paid}")
print(f"Change Due: {due}")
print("-------------------------------")