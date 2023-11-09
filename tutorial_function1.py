# write a pythone to find the upper case , lower case,charcter ,no of words
sentence = input("Enter the sentence:")
def upper(sentence):
    upper=0
    for i in sentence:
        if(i.isupper()):
            upper+=1
    return upper        
# verified

def lower(sentence):
    lower=0
    for i in sentence:
        if(i.islower()):
            lower+=1
    return lower        
# verified

def charec(sentence):
    chars=0
    for i in sentence:
        chars+=1
    return chars   
#verified 

def words(sentence):
    word=0
    for i in sentence:
        if(i==' '):
            word+=1
    return word 
#verified       

print(upper(sentence),lower(sentence),charec(sentence),words(sentence))
