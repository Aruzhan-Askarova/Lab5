def camel_to_snake(s):
    result = []
    
    for char in s:
        if char.isupper():
            result.append('_')  # Insert an underscore before the capital letter
            result.append(char.lower())  # Convert the capital letter to lowercase
        else:
            result.append(char)
    
    # Join the list into a string and remove any leading underscore
    return ''.join(result).lstrip('_')

# Example usage
input_string = "camelCaseToSnakeCase"
output_string = camel_to_snake(input_string)
print(output_string)
