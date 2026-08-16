f1=120
f2=85
f3=150
f4=95
f5=110
total=f1+f2+f3+f4+f5
avg=total/5
print("Total crop yeild: ", total)
print("Average crop yeild: ", avg)

pricepkg=15
totalearning=total*15
print("Total earnings: ", totalearning)

noofbags=total//25
leftover=total%25
print("Number of bags packed: ", noofbags)
print("Leftover crop: ", leftover)

lastcrop=500
print("Better than last year?: ", total>lastcrop)
print("Same as last year?: ", lastcrop==total)
print("Atleast as good?: ", total>=lastcrop)

bcrop=30
total+=bcrop
print("After adding bonus crop total:", total)
scrop=15
total-=scrop
print("After saving crop for next year total:", total)

fbag=total//25
print("Final bag count after all adjustments:", fbag)
