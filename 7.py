import re

def snake_to_camel(s):
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

test_string = 'hello_world_this_is_snake_case'
result = snake_to_camel(test_string)
print(result)
