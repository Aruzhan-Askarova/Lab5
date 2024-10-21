import re

def find_sequence(s):
    pattern = r'^[A-Z][a-z]+$'
    
    if re.match(pattern, s):
        return f"'{s}' matches the pattern"
    else:
        return f"'{s}' does not match the pattern"

test_strings = ['Hello', 'hello', 'HELLO', 'H', 'HelloWorld']
for s in test_strings:
    print(find_sequence(s))
