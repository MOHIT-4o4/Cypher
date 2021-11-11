"""Enrypting text with Fernet"""
from cryptography.fernet import Fernet
import pyttsx3
from pyttsx3 import engine


try :
    print("Cypher is Running...")
    # text = "This is a secret message"
    text = str(input("Enter the text you want to encrypt:"))
    #generate key
    key = Fernet.generate_key()
    #creating instance 
    fernet = Fernet(key)

    #using fernet class instance to encrypt string 
    encMessage = fernet.encrypt(text.encode())
    #print
    print(f"message before encryption: {text}")
    print(f"message after encryption: {encMessage}")
except Exception as error:
    engine= pyttsx3.init()
    engine.say(error)
    print("Error:",error)
    engine.runAndWait()
