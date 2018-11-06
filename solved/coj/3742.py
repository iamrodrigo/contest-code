import re

values = raw_input()

try:
    while values:
        words = 1;
        upperCase = 0;
        length = len(values)
        for i, c in enumerate(re.sub(r'\s+', ' ', values.strip())):
            if c == ' ':
                words += 1
            elif c.isupper():
                upperCase += 1    
                
        print("correct" if words == upperCase else "awful")
        values = raw_input()
except EOFError:
    exit

