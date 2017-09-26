import re
import itertools
from collections import Counter
import numpy as np
# todo add support of !

a = raw_input("Enter the number of elements: ")
lst = list(itertools.product([0, 1], repeat=int(a)))

def implication(a, b):
    if a == 0:
        return 1
    if a == 1 and b == 0:
        return 0
    if a == 1 and b == 1:
        return 1

def equiv(a, b):
    if a == b:
        return 1
    else:
        return 0

def conjunction(a, b):
    c = a * b
    return c

def disjunction(a, b):
    c  = a + b
    if c > 1:
        return 1
    else:
        return c

def is_number(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_name(str):
    return re.match("\w+", str)

def peek(stack):
    return stack[-1] if stack else None

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == "&&":
        values.append(conjunction(left, right))
    if operator == "||":
        values.append(disjunction(left, right))
    if operator == "-->":
        values.append(implication(left, right))
    if operator == "<-->":
        values.append(equiv(left, right))
    # values.append(eval("{0}{1}{2}".format(left, operator, right)))
def translate(expression):
    same = []

    lst = list(itertools.product([0, 1], repeat=int(a)))
    vars = re.findall("[A-Za-z]", expression)
    unique = list(set(vars))
    if len(unique) == len(lst[0]):
        for tuple in lst:
            for var, number in zip(unique, tuple):
                unique.insert(unique.index(var)+1, number)
            n_expr = expression.split(' ')
            for i in range(len(n_expr)):
                for index, var in enumerate(unique):
                    if n_expr[i] == var:
                        n_expr[i] = str(unique[index+1])
            # print " ".join(n_expr)
            print "Result: ", evaluate(" ".join(n_expr))
            unique = list(set(vars))





def evaluate(expression):
    tokens = re.findall("-->|<-->|&&|\|\||\(|\)|\d+", expression)
    values = []
    operators = []
    vl = 0
    for token in tokens:
        if is_number(token):
            vl += 1
            values.append(int(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            top = peek(operators)
            while top is not None and top != '(':
                apply_operator(operators, values)
                top = peek(operators)
            operators.pop() # Discard the '('
        else:
            # Operator
            top = peek(operators)
            while top is not None and top not in "()":
                apply_operator(operators, values)
                top = peek(operators)
            operators.append(token)
    while peek(operators) is not None:
        apply_operator(operators, values)
    return values[0]


def main():
    expression = raw_input("> ")
    translate(expression)
    #evaluate(expression)
    #print("Shunting Yard Algorithm: {0}".format(evaluate(expression)))

if __name__ == '__main__':
    main()

