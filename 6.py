import re

def replace_characters(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

test_string = 'Hello, world. How are you today?'
result = replace_characters(test_string)
print(result)
