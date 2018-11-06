from collections import deque

def checkInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def evalRPN(tokens):
    stack = deque()
    for token in tokens:
        temp = token
        if not checkInt(temp):
            b = stack.popleft()
            a = stack.popleft()
            if token == '+':
                temp = a + b
            elif token == '*':
                temp = a * b
            elif token == '/':
                temp = a/float(b)
            elif token == '-':
                temp = a-b

        stack.appendleft(int(temp))

    print stack.pop()

evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
evalRPN(["4", "13", "5", "/", "+"])
evalRPN(["2", "1", "+", "3", "*"])

