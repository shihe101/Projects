import re
# Import the regular expressions module

def password_strength(password):
    """Checks the strength of a given password."""
    
    # Define regex patterns to check for various password strength factors
    # Defines a regular expression pattern that matches any string that is at least 8 characters long
    # Assigns it to the variable length_regex

    length_regex = re.compile(r'.{8,}')  # Password length should be at least 8 characters
    upper_regex = re.compile(r'[A-Z]')   # Password should contain at least one uppercase letter
    lower_regex = re.compile(r'[a-z]')   # Password should contain at least one lowercase letter
    digit_regex = re.compile(r'\d')      # Password should contain at least one digit
    special_regex = re.compile(r'[\W_]') # Password should contain at least one special character

    # Defines a regular expression pattern that matches any non-word character 
    # Any character that is not a letter, digit, or underscore) 
    # Assigns it to the variable

    # Check each regex pattern against the password and calculate a strength score
    # Check if the password meets the length requirement, and add 1 to the score if it does
    
    score = 0
    if length_regex.search(password):
        score += 1
    if upper_regex.search(password):
        score += 1
    if lower_regex.search(password):
        score += 1
    if digit_regex.search(password):
        score += 1
    if special_regex.search(password):
        score += 1
    
    # Determine the strength of the password based on its score
    if score == 0:
        strength = 'very weak'
    elif score == 1:
        strength = 'weak'
    elif score == 2:
        strength = 'medium'
    elif score == 3:
        strength = 'strong'
    elif score == 4:
        strength = 'very strong'
    else:
        strength = 'invalid'
    
    return strength

# Example usage
password = input('Enter a password: ')
strength = password_strength(password)
print('Password strength:', strength)