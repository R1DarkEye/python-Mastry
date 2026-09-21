import re
from collections import Counter


def zero(operation=None): return 0 if operation is None else operation(0)
def one(operation=None): return 1 if operation is None else operation(1)
def two(operation=None): return 2 if operation is None else operation(2)
def three(operation=None): return 3 if operation is None else operation(3)
def four(operation=None): return 4 if operation is None else operation(4)
def five(operation=None): return 5 if operation is None else operation(5)
def six(operation=None): return 6 if operation is None else operation(6)
def seven(operation=None): return 7 if operation is None else operation(7)
def eight(operation=None): return 8 if operation is None else operation(8)
def nine(operation=None): return 9 if operation is None else operation(9)

def plus(number): return lambda x: x + number
def minus(number): return lambda x: x - number
def times(number): return lambda x: x * number
def divided_by(number): return lambda x: x // number

# =================================================
def same_structure_as(original,other): #will improve it tomorrow or else at least think of solution
    if(len(original)!=len(other)):
         return False
    ori_size=[]
    other_size=[]
    for i in original:
        if(type(i)==type(original)):
            ori_size.append(len(i))
        else:
            ori_size.append(1)
    for j in other:
            if(type(j)==type(original)):
                other_size.append(len(j))
            else:
                other_size.append(1)
    return other_size==ori_size

# =================================================
def same_structure_as_1(original,other):
    if len(original) != len(other):
        return False
    for i in range(len(original)):
        if isinstance(original[i], list) and isinstance(other[i], list):
            if not same_structure_as(original[i], other[i]):
                return False
        elif isinstance(original[i], list) or isinstance(other[i], list):
            return False
    return True

# =================================================
def top_3_words(text):
    import re
    from collections import Counter

    words = re.findall(r"[a-z']*[a-z][a-z']*", text.lower())
    return [word for word, _ in Counter(words).most_common(3)]
def parse_int(string):
    small_numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }
    current = 0
    total = 0

    for word in string.lower().replace("-", " ").split():
        if word == "and":
            continue
        if word in small_numbers:
            current += small_numbers[word]
        elif word == "hundred":
            current *= 100
        elif word == "thousand":
            total += current * 1000
            current = 0
        elif word == "million":
            total += current * 1_000_000
            current = 0

    return total + current

def score(dice):
    from collections import Counter
    counts = Counter(dice)
    score = 0

    # Check for three of a kind
    for num in range(1, 7):
        if counts[num] >= 3:
            if num == 1:
                score += 1000
            else:
                score += num * 100
            counts[num] -= 3

    # Add points for remaining ones and fives
    score += counts[1] * 100
    score += counts[5] * 50

    return score

def tree_by_levels(node):
    if node is None:
        return []

    values = []
    queue = [node]
    index = 0

    while index < len(queue):
        current = queue[index]
        index += 1
        values.append(current.value)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return values