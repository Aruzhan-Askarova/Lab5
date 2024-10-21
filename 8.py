import re

def split_at_uppercase(s):
    pattern = r'(?=[A-Z])'
    return re.split(pattern, s)

test_string = 'HelloWorldThisIsPython'
result = split_at_uppercase(test_string)
print(result)
