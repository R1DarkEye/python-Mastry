def bool_to_word(boolean):
    # TODO
    if(boolean):
        return "Yes"
    else:
        return "No"
# ----------------------------------------------
def better_than_average(class_points, your_points):
    # Your code here
    total=0
    for i in class_points:
        total+=i
    avg=total/len(class_points)
    return True if your_points>avg else False
# ------------------------------------------
def rps(p1, p2):
    #your code here
    if (p1=="paper" and p2=="rock"):
        return "Player 1 won!"
    elif(p1=="rock" and p2=="paper"):
        return "Player 2 won!"
    elif(p1=="scissors" and p2=="paper"):
        return "Player 1 won!"
    elif(p2=="scissors" and p1=="paper"):
        return "Player 2 won!"
    elif(p2=="scissors" and p1=="rock"):
        return "Player 1 won!"
    elif(p1=="scissors" and p2=="rock"):
        return "Player 2 won!"
    else:
        return "Draw!"
# -------------------------------------------------
def hero(bullets, dragons):
    return True if int(bullets//2)>=dragons else False
# ----------------------------------------------------
def square_sum(numbers):
    #your code here
    total=0
    for i in numbers:
        total+=i*i
    return total
# ------------------------------------------------------
def find_smallest_int(arr):
    # Code here
    return min(arr)
# --------------------------------------------------------
def check(seq, elem):
    for x in seq:
        if(x==elem):
            return True
    return False
# ------------------------------------------------------------
def feast(beast, dish):
    # your code here
    return True if beast[0]==dish[0] and beast[-1]==dish[-1] else False
# --------------------------------------------------------------------
def string_to_number(s):
    # your code here
    return int(s)
# --------------------------------------------------------------------
def filter_list(l):
    s=[]
    for i in l :
        if(type(i)==int):
            s.append(i)
    return s
# --------------------------------------------------------------------
def make_negative( number ):
    return -abs(number)
    return number if number>0 else number-(number*2)
#  or 
# def make_negative( number ):
#   return -abs(number)
# --------------------------------------------------------------------
def positive_sum(arr):
    # Your code here
    return sum(i for i in arr if i>0)
# --------------------------------------------------------------------
def grow(arr):
    s=1
    for x in arr:
        s*=x
# --------------------------------------------------------------------
def odd_or_even(arr):
    return "even" if sum(arr)%2==0 else "odd"
