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
# A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.

# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.
def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    count = 1
    while h * bounce > window:
        count += 2
        h *= bounce
    return count

# --------------------------------------------
def order(sentence):
    if sentence == "":
        return ""
    words = sentence.split()
    sorted_words = sorted(words, key=lambda x: sorted(x))
    return " ".join(sorted_words)
# --------------------------------------------
def to_camel_case(text):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(text.replace('-', ' ').replace('_', ' ').split()))

# --------------------------------------------

def spin_words(sentence):
    return ' '.join([word[::-1] if len(word) >=5 else word for word in sentence.split()])

# spin_words("Hey fellow warriors")
# --------------------------------------------
def rot13(message):
    result = ""
    for char in message:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result
