import re

def match_string(s):
    pattern = r'^ab*$'
    
    if re.match(pattern, s):
        return f"'{s}' matches the pattern"
    else:
        return f"'{s}' does not match the pattern"

test_strings = ['a', 'ab', 'abb', 'abbb', 'b', 'abc']
for s in test_strings:
    print(match_string(s))
