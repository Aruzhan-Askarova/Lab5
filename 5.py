import re

def match_string(s):
    pattern = r'^a.*b$'
    
    if re.match(pattern, s):
        return f"'{s}' matches the pattern"
    else:
        return f"'{s}' does not match the pattern"

test_strings = ['ab', 'a123b', 'acb', 'a', 'b', 'axb']
for s in test_strings:
    print(match_string(s))
