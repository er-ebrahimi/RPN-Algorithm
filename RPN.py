# from curses.ascii import isdigit
# input('hello')
# try:
from typing import List


operator = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4,
            'tan(': 1, 'cos(': 1, 'sin(': 1, 'ln(': 1, 'abs(': 1, 'exp(': 1}
exper = input().split()
stack = []
stack.append(exper[1])
postfix = []
postfix.append(exper[0])
for i in range(2, len(exper)):
    try:
        if float(exper[i]):
            postfix.append(float(exper[i]))
            continue
    except ValueError:
        pass
    if exper[i] == '(':
        stack.append(exper[i])
    elif exper[i] == ')':
        for j in range(0, stack, -1):
            if not '(' in stack[i]:
                postfix.append(stack.pop(i))
    elif operator[exper[i]] <= operator[stack[len(stack) - 1]]:
        postfix.append(stack.pop())
        stack.append(exper[i])
    else:
        stack.append(exper[i])
for i in range(len(stack)):
    postfix.append(stack.pop())
num = []

# except:
#     print('reject')
# 10 / 2 + 4 * -3.5
