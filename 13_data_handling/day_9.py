import base64
import os
VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()
    

def decode(text):
    return base64.b64decode(text.encode()).decode()
    

def password_strength(password):
   length = len(password)
   has_upper = any(c.isupper() for c in password)
   has_digit = any(c.isdigit() for c in password)
   has_special = any(c in "!@#$%^&*().,<>" for c in password)
   
   score = sum([length >= 8, has_upper, has_digit, has_special])
   return ["Weak", "Medium", "Strong", "Very Strong"][min(score, 3)]
   


def add_credential():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    strength = password_strength(password)
    
    print(f"Password Strength: {strength}")
    
    line = f"{website}||{username}||{password}"
    
    encoded_line = encode(line)
    
    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")
        
    print("Credentials Saved")


def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File Not Found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_password = '*' * len(password)
            print(f"{website} | {username} | {hidden_password}")


def main():
    while True:
        print("Credentials Manager")
        print("1. Add Credential")
        print("2. View Credentials")
        # print("3. Update Password")
        print("4. Exit")
        
        choice = input("Enter your choice : ")
        
        match choice:
            case "1":
                add_credential()
            case "2":
                view_credentials()
            case "4":
                break
            case _:
                print("Invalid Choice")
                
   

if __name__ == "__main__":
    main()