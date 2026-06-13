

import string
import random
import getpass


def check_password_strength(password):
    issues = []
    if len(password) < 8:
        issues.append("Password must be at least 8 characters long.")
    if not any(c.islower() for c in password):
        issues.append("Missing lowercase letter.")
    if not any(c.isupper() for c in password):
        issues.append("Missing uppercase letter.")
    if not any(c.isdigit() for c in password):
        issues.append("Missing digit.")
    if not any(c in string.punctuation for c in password):
        issues.append("Missing special character.")
    return issues



def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))       # Ensure at least one character from each category


password = getpass.getpass("Enter a password to check its strength: ")

issues = check_password_strength(password)

if not issues:
    print("Password is strong.")

else:
    print("Password is weak. Issues found:")
    
    for issue in issues:
        print(f" - {issue}")
        

suggestion = generate_strong_password()
print("\n suggesting you a strong password:")
print(suggestion)