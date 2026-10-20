items=["pencil","eraser","notebook","sharpner", "glue"]
stockcount=[12, 0, 8, 5, 3]

inventory={item: count for item, count in zip(items,stockcount)}
print("FULL INVENTORY: ")
print(inventory)

instockitem=[item for item in items if inventory[item] > 0]
print("ITEMS IN STOCK: ")
print(instockitem)

chosenitem=input("WHICH ITEM DO YOU WANT TO BUY?: ").strip().lower()
if chosenitem not in inventory or inventory[chosenitem]==0:
    print(f"{chosenitem} IS OUT OF STOCK.")
    exit()

prices=[10, 5, 40, 15, 20]
markup=int(input("ENTER THE MARK UP AMOUNT TO ADD TO EVERY PRICE: "))
markupprices=list(map(lambda p: p +markup, prices))
print("MARKUP PRICES: ")
print(markupprices)

itemindex=items.index(chosenitem)
chosenprice=markupprices[itemindex]
print(f"PRICE OF {chosenitem} AFTER MARKUP: ", chosenprice)

inventory[chosenitem] -= 1
print(chosenitem, "purchased!!")
print("remaining stock", inventory[chosenitem])

print("--------------SCHOOL STORE INVENTORY CHECKER------------------")
print("ITEM BOUGHT: ", chosenitem)
print("PRICE PAID: ", chosenprice)
print("UPDATED INVENTORY: ", inventory)
print("--------------------------------------------------------------")