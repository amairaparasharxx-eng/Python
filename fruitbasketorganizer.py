basket1={"apple","banana","mango", "pineapple", "kiwi", "apple"}
basket2={"watermelon", "strawberry", "mango", "apple"}
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)

basket1.add("orange")
print("Basket 1 after adding orange: ", basket1)

commonfruits= basket1.intersection(basket2)
print("The Common Fruits in Basket 1 and 2: ", commonfruits)

allfruits= basket2.union(basket1)
print("All the fruits: ", allfruits)

import array as arr
fruitcount= arr.array("i", [3, 5, 2, 4])
print("Fruit Count Array: ", fruitcount)

fruitcount.insert(0,1)
fruitcount.append(6)
print("Fruit Count Array after Adding Items: ", fruitcount)

count4= fruitcount.count(4)
print("The Number of 4's in Fruit Count Array: ", count4)

fruitcount.reverse()
print("Reversed Fruit Count Array: ", fruitcount)

print("================FRUIT BASKET ORGANIZER==================")
print("Basket 1: ", basket1)
print("Basket 2: ", basket2)
print("Basket 1 after adding orange: ", basket1)
print("The Common Fruits in Basket 1 and 2: ", commonfruits)
print("All the fruits: ", allfruits)
print("Fruit Count Array: ", fruitcount)
print("========================================================")