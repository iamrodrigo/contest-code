operatorValues = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0}
operandToValues = {}
operator = []
total = []
postfix = ""

a = raw_input()
values = raw_input()

try:
    while values:
        operandToValues[values[0]] = float(values[2:])
        values = raw_input()
except EOFError:# Do nothing
    pass

def solve():
    s = postfix[-1]
    b = total.pop()
    a = total.pop()
    t = 0
    if s == '+':
        t = a + b
    elif s == '-':
        t = a - b
    elif s == '*':
        t = a * b
    elif s == '^':
        t = a ** b
    elif s == '/':
        t = a / b
    total.append(t)

def ishigherPrecedence(poppedElement, operator):
    return operatorValues[operator] <= operatorValues[poppedElement]

for c in a:
    if c.isalpha():
        postfix += c
        total.append(operandToValues[c])
    elif c == ')':
        while len(operator) and operator[-1] != '(':
            postfix += operator.pop()
            solve()
        operator.pop()
    elif c == '(':
        operator.append(c)
    else:
        while len(operator) and ishigherPrecedence(operator[-1], c):
            postfix += operator.pop()
            solve()
        operator.append(c)

while len(operator):
    postfix += operator.pop()
    solve()

print postfix
print "{0:.2f}".format(total.pop())