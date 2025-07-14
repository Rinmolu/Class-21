def matchwords(words):
    ctr=0
    list=[]
    for word in words:
        if len(word) >1 and word[0] == word[-1]:
            ctr=ctr+1
            list.append(word)
    print("List Of Words With First And Last Characters The Same. ",list)
    return ctr 
count=matchwords(["ABCA", "Dog", "Mat", "ABABA"])
print("Numbers Of Words Having First And Last Characters The Same. ",count)