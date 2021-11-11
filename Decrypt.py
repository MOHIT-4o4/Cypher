from cryptography.fernet import Fernet
import pyttsx3
from pyttsx3 import engine
#generate key
try:
    key = Fernet.generate_key()
    #creating instance 
    f = Fernet(key)

    token = f.encrypt("This is a message".encode())
    print("Message after encryption: ",token)
    #after we encrypt out text it gave us output in bytes as same as in decryption we can remove that by 
    # encode and decode method  
    d = f.decrypt(token).decode()
    print(f"message after decryption: ",d)
except Exception as error:
    engine = pyttsx3.init()
    engine.say(error)
    engine.runAndWait()
    print("Error", error)

