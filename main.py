from cryptography.fernet import Fernet
import os

KEY_FILE = "key.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

key = load_key()
fernet = Fernet(key)

# print("Encryption system ready.")
# test_password = "mysecret123"

encrypted = fernet.encrypt(test_password.encode())
decrypted = fernet.decrypt(encrypted).decode()

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
import json

DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)
def add_password():
    site = input("Enter site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    encrypted_password = fernet.encrypt(password.encode()).decode()

    data = load_data()

    data[site] = {
        "username": username,
        "password": encrypted_password
    }

    save_data(data)

    print("Password saved successfully!")
def view_password():
    site = input("Enter site name: ")

    data = load_data()

    if site in data:
        encrypted_password = data[site]["password"]
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

        print("Username:", data[site]["username"])
        print("Password:", decrypted_password)
    else:
        print("No entry found.")
def main():
    while True:
        print("\n=== PASSWORD MANAGER ===")
        print("1. Add Password")
        print("2. View Password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
