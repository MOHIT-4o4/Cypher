from cryptography.fernet import Fernet
#generate key
key = Fernet.generate_key()
#creating instance 
f = Fernet(key)

token = f.encrypt("This is a message".encode())
print("Message after encryption: ",token)
#after we encrypt out text it gave us output in bytes as same as in decryption we can remove that by 
# encode and decode method  
d = f.decrypt(token).decode()
print(f"message after decryption: ",d)


