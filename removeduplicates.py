studentdata={"id1":{"name":"Sara", "class":"V","subject":"english, math, science"},
             "id2":{"name":"David", "class":"V","subject":"english, math, science"},
             "id3":{"name": "Sara", "class":"V","subject":"english, math, science"}, 
             "id4":{"name":"Surya", "class":"V","subject":"english, math, science"}
             }
result={}
seenkey=[]
for studentid,details in studentdata.items():
    unique_key=(details["name"], details["class"], details["subject"])
    if unique_key not in seenkey:
        seenkey.append(unique_key)
        result[studentid]=details
for k,v in result.items():
    print(k,":", v)
