from cryptography.fernet import Fernet
# import database

# Create connection object

# Create key
class PasswordManager:
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self,path):
        self.key = Fernet.generate_key()

f = Fernet(key)

token = f.encrypt(b"my deep dark secret")

print(token)
b'...'

print(f.decrypt(token))
b'my deep dark secret'

