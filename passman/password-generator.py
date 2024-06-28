import random
import string
import hashlib

class Account:
    def __init__(self,user="",password=""):
        self.website = ""
        self.user = user
        self.password = password
    # Prompt for credentials
    def enter_credentials(self):
        self.website = input("Website name:" )
        self.user = input("Enter account username: ")
        self.password = input("Enter account password:")
    
    def display_credentials(self):
        print(f"Website: {self.website}") 
        print(f"Username: {self.user}") 
        print(f"Password: {self.password}") 

    def create_password():
        account = Account()
        account.enter_credentials()
        account.display_credentials()
    
alpha = list(string.ascii_letters)
num = list(string.digits)
special_char = ['!','?',';','.','^','$','#','@','&','+']
 
# Salt factory
salt = ""
size = 5
for s in range(0, size):
    salt += random.choice(alpha)
    
#add functionality to add salt to the end instead
    
 # Regular password generator...
def generate_pass():
    length = int(input("Enter password desired length:"))
    if (length >= 3 and length < 123):
        word = generate_pass_helper(length)
        return scramble(word)
    else:
        print("must be at least 3 characters in length")


'''Fixed it but ... eventually I think I will have to make it
so that it combines the salt with the unhashed password when I am going to implement a 'copy password' feature. 
'''
def generate_pass_helper(n):
    word = ""
    options = [alpha, num, special_char]
    for x in range(0,n):
        pick = random.randint(0,2)
        type = random.choice(options[pick])
        word += random.choice(type)
    return word
# Hashing
def encrypt_password(word):
    # example
    m = hashlib.sha224(b"grah").hexdigest()
    # take in the string (password)
    ptext = word
    # apply hash
    result = str(hashlib.sha224(b"ptext").hexdigest())
    print(result)
    # store in database
''' How do I get the password after it is stored, unhashed???'''
    #storeinDB()
def decrypt_password():
    pass
if __name__ == "__main__":
    word = generate_pass()
    # password = salt + word
    #print(password)