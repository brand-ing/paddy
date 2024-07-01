# Imports
import re
# Key Functionality: 
# - Use password standards
# - Smart Suggestions on how to improve it with indicator
# - Later when I database password, have a timer to remind the user to update their password every 30, 45, 90 days OR they can put in reminders for passwords that expire
# - User can export passwords though we strongly recommend against this
# - User education


def CheckPasswordComplexity():
    # Requirements with regex
    requires_uppercase = re.compile('[A-Z]')
    requires_digit = re.compile('\d')
    requires_lowercase = re.compile('[a-z]')
    
    # length
    min_length = 8

    # checks

    # if all checks pass
    return "Strong"


