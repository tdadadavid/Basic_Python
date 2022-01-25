
fWord  = ["fuck" , "shit"]

sentence = "what the fuck is going on"
# result should be "what the f**k is going on"


def filterWords(s):
    s = list(s)
    for i in s:
        if s[i] == "fuck" or s[i] == "shit":
            s[i] = "****"
    
    return  s       
        
    
print(filterWords(sentence))    