rowsize=int(input("Enter the row size: "))
if rowsize%2==0:
    halfdiamond=int(rowsize/2)
else:
    halfdiamond=int(rowsize/2)+1
space=halfdiamond-1

for i in range(1, halfdiamond+1):
    for j in range(1, space+1):
        print(end=" ")
    space-=1
    number=1
    for j in range(2*i-1):
        print(end=str(number))
        number+=1
    print()
space=1
for i in range(1, halfdiamond):
    for j in range(1, space+1):
        print(end=" ")
    space+=1 
    number=1
    for j in range(1, 2*(halfdiamond-i)):
        print(end=str(number))
        number+=1
    print()