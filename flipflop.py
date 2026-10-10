def palindome(r):
    e=len(r)-1
    s=0
    while s<e:
        if (r[s]!=r[e]):
            return False
        e-=1
        s+=1
    return True

r=(1,2,3,5,5,3,2,1)
if palindome(r):
    print("Tuple is a palindrome!!")
else:
    print("Tuple is not a palindrome...")
