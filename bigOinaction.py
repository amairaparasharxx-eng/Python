n=10
guess=input("Double Loop at n=10 checks n x n pairs. How many? ")
input("Formula: One calculation done. Press enter to run.")
steps=1
print(f" steps= {steps} -> O(1) constant time -> steps never change.")

input("Loop: one step per item. Press enter to run.")
steps=0
for i in range(n):
    steps+=1
print(f"    steps= {steps}  -> O(n) linear time -> steps grow with n.")

input("Double Loop: checks every pair. Press enter to run.")
steps=0
for i in range (n):
    for j in range(n):
        steps+=1
print(f"    steps= {steps}  -> your guess: {guess}  -> O(n^2)   -> quadratic time")