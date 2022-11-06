from cryptography.fernet import Fernet
import subprocess,os
def encrypt(filename):
    binary = "";
    with open(f"./{filename}","rb") as file:
        binary = file.read();
    key = "WY2-h3K8Mjm8fpfRJTKHe9Y18dkIIETiQlmGKGhrZpQ="
    fernet = Fernet(key)
    encrypted = fernet.encrypt(binary)
    with open(f"{filename}.exp","wb") as file:
        file.write(encrypted)
    subprocess.run(["rm","-rf",f'{filename}'])
filename = input("Filename : ")
encrypt(filename)