from cryptography.fernet import Fernet
def load_key():
    file = open ("key,key", "rb")
    key = file.read()
    file.close()
    return key
key = load_key()
fer = Fernet(key)

fer = Fernet(key)
def write_key():
    key = Fernet.generate_key()
    with open("key.key" ,"wb") as key_file:
        key_file.write(key)

def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("user:", user,"| password",
            fer.decrypt(passw.encode()).decode())

def add():
    names = input("Account Name: ")
    pwd  = input("password: ")
    with open('password.txt', 'a') as f:
        f.write(names +"|" + pwd + "\n")



while True:
    made = input("would you like to add a new pasword or view exisiting ones (view, add) press q to quit?").lower()
    if made == "q":
        break
    
    if made == "view":
        view()
    elif made == "add":
        add()
    else:
        print("invalid mode. ")
        continue