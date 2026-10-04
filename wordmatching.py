print("Match the word, if first and last letter is same. Then add this word to a new list.")

def matchingword(words):
    counter=0
    list1=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            counter+=1
            list1.append(word)
            print("The first and last letter is the same.")
            print(f"The new list is {list1} and counter is at {counter}.\n")

count=matchingword(['hannah', '276', '9679', '543', '878', 'race', 'inside'])
