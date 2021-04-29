dict={}

def count(word):
    chars=list(word)
    for c in chars:
        if c in dict:
            dict[c]+=1
        else:
            dict[c]=1

def most_frequent(string):
    split_words=string.split()
    for word in split_words:
        count(word)
    for x,v in sorted(dict.items(),key=lambda item:item[1],reverse=True):
        print(x,"=",v)
most_frequent(input("Enter the string:"))
