from cryptography.fernet import Fernet
import subprocess,os,sys
 
def encrypt(filename):
    binary = "";
    with open(f"./{filename}","rb") as file:
        binary = file.read();
    key = "WY2-h3K8Mjm8fpfRJTKHe9Y18dkIIETiQlmGKGhrZpQ="
    fernet = Fernet(key)
    encrypted = fernet.encrypt(binary)
    with open(f"{filename}.exp","wb") as file:
        file.write(encrypted)
def drm():
    return True
def run(filename):
    exten = filename.split(".")[-1]
    if(exten==filename):
        proc =  subprocess.run(f'./{filename}',capture_output=True)
        print(proc.stdout);
    elif (exten== "pdf"):
        proc =  subprocess.run(["evince",f'./{filename}'],capture_output=True)
        print(proc.stdout);
def decrpytNexec(filename):
    if(not(drm())):
        return
    key = "WY2-h3K8Mjm8fpfRJTKHe9Y18dkIIETiQlmGKGhrZpQ="
    fernet = Fernet(key)
    encrypted="";
    with open(f'./{filename}', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(f'{filename[:-4]}', 'wb') as dec_file:
        dec_file.write(decrypted)
    subprocess.run(["chmod","+x",f'{filename[:-4]}'])
    run(filename[:-4])
    subprocess.run(["rm","-rf",f'{filename[:-4]}'],capture_output=True)

def findEncrpted():
    for file in os.listdir(os.getcwd()):
        if file[-4:] == ".exp":
            return file
    else:
        print("No file to execute")
        sys.exit()
filename = findEncrpted()
decrpytNexec(filename)