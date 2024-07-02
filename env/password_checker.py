# Imports
import re
# Key Functionality: 
# - Use password standards
# - Smart Suggestions on how to improve it with indicator
# - Later when I database password, have a timer to remind the user to update their password every 30, 45, 90 days OR they can put in reminders for passwords that expire
# - User can export passwords though we strongly recommend against this
# - User education


def CheckPasswordComplexity(password):
    # Requirements with regex
    # length
    min_length = 8
    # contains
    requires_uppercase = re.compile(r'[A-Z]')
    requires_digit = re.compile(r'\d')
    requires_lowercase = re.compile(r'[a-z]')
    # we want special characters too.
    requires_special_character = re.compile(r'[@$!%*?&]')

    # checks
    if not requires_uppercase.search(password):
        return "Password must contain at least one uppercase letter."
    
    if not requires_lowercase.search(password):
        return "Password must contain at least one lowercase letter."
    
    if not requires_digit.search(password):
        return "Password must contain at least one digit."
    
    if not requires_special_character.search(password):
        return "Password must contain at least one special character."
    
    # if all checks pass
    return "Strong"


# Example usage
password = "Password1!"
result = CheckPasswordComplexity(password)
print(result)