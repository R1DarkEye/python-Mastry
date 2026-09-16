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

