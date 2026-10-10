weather=(0,1,1,0,0,1,1,0,1,0,0)
sunny=0
rainy=0
for i in range(0,11):
    if weather[i]==0:
        sunny+=1
    else:
        rainy+=1

if sunny>rainy:
    print("It is good weather!!")
else:
    print("It is bad weather!!")