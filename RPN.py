# from curses.ascii import isdigit
# input('hello')
# try:

from turtle import pos
from typing import List
import math
import numpy
from traitlets import Instance
from numpy import log as ln

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
print(postfix)
num = []
for i in range(len(postfix)):
    try:
        if float(postfix[i]):
            num.append(float(postfix[i]))
            continue
    except ValueError:
        pass
    if postfix[i] == '*':
        temp = num.pop()
        num.append(num.pop() * temp)
    elif postfix[i] == '/':
        temp = num.pop()
        num.append(num.pop() / temp)
    elif postfix[i] == '+':
        temp = num.pop()
        num.append(num.pop() + temp)
    elif postfix[i] == '-':
        temp = num.pop()
        num.append(num.pop() - temp)
    elif postfix[i] == 'sin(':
        num.append(math.sin(num.pop()))
    elif postfix[i] == 'cos(':
        num.append(math.cos(num.pop()))
    elif postfix[i] == 'tan(':
        num.append(math.tan(num.pop()))
    elif postfix[i] == 'ln(':
        num.append(math.log(10, num.pop()))
    elif postfix[i] == 'abs(':
        num.append(abs(num.pop()))
    elif postfix[i] == '^':
        num.append(num.pop() ** num.pop())
    elif postfix[i] == 'exp(':
        num.pop(math.exp(num.pop()))
format_float = "{:.2f}".format(num[0])
print(format_float)
