dict1={"Codingal": 2, "is": 1, "best":2, "for": 2, "coding": 1}
print("The original dictionary: " + str(dict1))

k=2
result=0
for key in dict1:
    if dict1[key] == k:
        result+=1
print(f"The frequency of 2: "+ str(result))