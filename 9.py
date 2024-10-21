def insert_spaces(s):
    result = []
    
    for i, char in enumerate(s):
        if char.isupper() and i != 0:
            result.append(' ')  # Insert a space before the capital letter
        result.append(char)
    
    return ''.join(result)

# Example usage
input_string = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
output_string = insert_spaces(input_string)
print(output_string)
