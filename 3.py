import re

def find_sequences(s):
    pattern = r'^[a-z]+_[a-z]+$'
    
    if re.match(pattern, s):
        return f"'{s}' matches the pattern"
    else:
        return f"'{s}' does not match the pattern"

test_strings = ['abc_def', 'abc', 'ABC_DEF', 'abc_def_ghi', 'abc_d']
for s in test_strings:
    print(find_sequences(s))
