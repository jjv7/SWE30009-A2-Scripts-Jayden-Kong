import sys

def split_alphabets(char_list):
    lowercase_list = []
    uppercase_list = []
    
    for char in char_list:
        if char.isalpha():
            if char.isupper():
                uppercase_list.append(char)
            elif char.islower():
                lowercase_list.append(char)
    
    lowercase_list = sorted(lowercase_list)
    uppercase_list = sorted(uppercase_list)
    
    return lowercase_list, uppercase_list

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python program.py <character1> <character2> ...")
        print("Example: python program.py C a b Z c")
        print("Note: Non-alphabetic characters are ignored.")
        sys.exit(1)
    
    input_chars = sys.argv[1:]
    non_alpha = [char for char in input_chars if not char.isalpha()]
    if non_alpha:
        print(f"Warning: Non-alphabetic characters {non_alpha} will be ignored.")
    
    lower, upper = split_alphabets(input_chars)
    print(f"Uppercase: {upper}")
    print(f"Lowercase: {lower}")
    