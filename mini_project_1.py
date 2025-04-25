password = input("Enter the password: ")

def csc(password):
    special_chars = {'@', '#', '$', '%', '&', '*', '!'}
    
    upper = 0
    lower = 0
    special_count = 0
    special_dict = {'@': 0, '#': 0, '$': 0, '%': 0, '!': 0, '&': 0, '*': 0}

    for char in password:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        if char in special_chars:
            special_count += 1
            if char in special_dict:
                special_dict[char] += 1

    result = {
        'Capital letters': upper,
        'Lowercase letters': lower,
        'Length of password': len(password),
        'Total special characters': special_count,
        'Special character counts': {k: str(v) for k, v in special_dict.items() if v > 0}
    }

    return result

# Print the result
print("\n--- Password Analysis ---")
for key, value in csc(password).items():
    print(f"{key}: {value}")