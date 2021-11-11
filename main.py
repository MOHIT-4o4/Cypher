from cryptography.fernet import Fernet

text = "This is a secret message"
#generate key
key = Fernet.generate_key()
#creating instance 
fernet = Fernet(key)

#using fernet class instance to encrypt string 
encMessage = fernet.encrypt(text.encode())
#print
print(f"message before encryption:{text}")
print(f"message after encryption:{encMessage}")