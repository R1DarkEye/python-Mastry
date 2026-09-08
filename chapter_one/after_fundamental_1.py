def duplicate_encode(word):
    word=word.lower()
    s=""
    for i in word:
        if word.count(i)>1:
            s+=")"
        else:
            s+="("
    return s
# --------------------------------------------
def is_valid_walk(walk):
    if(len(walk)<10 or len(walk)>10):
        return False
    x=0
    y=0
    for i in walk:
        if(i=="n"):
            x=x+1
        elif(i=="s"):
            x=x-1
        elif(i=="e"):
            y=y+1
        elif(i=="w"):
            y=y-1
    return True if x==0 and y==0 else False
# --------------------------------------------
def find_outlier(integers):
    if(integers[1]%2==0 and integers[0]%2==0 or integers[2]%2==0)